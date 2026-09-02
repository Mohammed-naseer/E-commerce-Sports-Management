from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from decimal import Decimal

from .models import Category, Product, Order, OrderItem, ContactSubmission, Delivery
from .forms import DeliveryForm, ContactForm
from .cart import Cart

def index(request):
    featured_products = Product.objects.filter(is_featured=True)[:8]
    categories = Category.objects.all()
    return render(request, 'base/index.html', {
        'featured_products': featured_products,
        'categories': categories,
    })

def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()
    query = request.GET.get('q', '').strip()
    sort = request.GET.get('sort', '')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(brand__icontains=query) |
            Q(category__name__icontains=query) |
            Q(category__department__icontains=query)
        )

    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')
    else:
        products = products.order_by('-created_at')

    return render(request, 'base/product_list.html', {
        'category': category,
        'products': products,
        'query': query,
        'sort': sort,
    })

# Specific category views for direct routing
def jersey(request):
    return product_list(request, category_slug='jersey')

def shoes(request):
    return product_list(request, category_slug='shoes')

def accessories(request):
    return product_list(request, category_slug='accessories')

def maleRunningShoes(request):
    return product_list(request, category_slug='male-running')

def femaleRunningShoes(request):
    return product_list(request, category_slug='female-running')

def trainingmen(request):
    return product_list(request, category_slug='training-men')

def trainingwomen(request):
    return product_list(request, category_slug='training-women')

def trainingKids(request):
    return product_list(request, category_slug='training-kids')


# Cart Views
def cart_view(request):
    cart = Cart(request)
    return render(request, 'base/cart.html', {
        'cart': cart,
        'cart_total': cart.get_total_price(),
    })

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        size = request.POST.get('size', 'Standard')
        quantity = int(request.POST.get('quantity', 1))
    else:
        size = request.GET.get('size', 'Standard')
        quantity = int(request.GET.get('quantity', 1))

    cart.add(product=product, size=size, quantity=quantity)
    messages.success(request, f"Added {product.name} ({size}) to your cart!")

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'status': 'success',
            'message': f"Added {product.name} to cart!",
            'cart_count': len(cart),
            'cart_total': str(cart.get_total_price())
        })

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or 'cart'
    return redirect(next_url)

def cart_remove(request, product_id):
    cart = Cart(request)
    size = request.GET.get('size', request.POST.get('size', 'Standard'))
    cart.remove(product_id=product_id, size=size)
    messages.info(request, "Item removed from cart.")

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(cart),
            'cart_total': str(cart.get_total_price())
        })

    return redirect('cart')

def cart_update(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        size = request.POST.get('size', 'Standard')
        quantity = int(request.POST.get('quantity', 1))

        cart.update_quantity(product_id=product_id, size=size, quantity=quantity)

        # calculate item total
        item_total = "0.00"
        for item in cart:
            if str(item['product_id']) == str(product_id) and item['size'] == size:
                item_total = f"{item['total_price']:.2f}"
                break

        return JsonResponse({
            'status': 'success',
            'item_total': item_total,
            'cart_count': len(cart),
            'cart_total': f"{cart.get_total_price():.2f}"
        })

    return redirect('cart')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, "Your cart has been cleared.")
    return redirect('cart')


# Checkout & Delivery
def deliveryForm(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your shopping cart is empty! Add products before proceeding to checkout.")
        return redirect('jersey')

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data.get('company', '')
            phone = form.cleaned_data['phoneno']
            address1 = form.cleaned_data['address']
            address2 = form.cleaned_data.get('address2', '')
            address3 = form.cleaned_data.get('address3', '')
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            postalcode = form.cleaned_data['postalcode']
            billing_same = form.cleaned_data.get('billing_same', False)

            total_amount = cart.get_total_price()

            # Create Order
            order = Order.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                address1=address1,
                address2=address2,
                address3=address3,
                state=state,
                city=city,
                postalcode=postalcode,
                billing_same=billing_same,
                total_amount=total_amount,
                status='Pending'
            )

            # Create OrderItems
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['name'],
                    image_name=item['image_name'],
                    size=item['size'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # Save to Delivery address book
            Delivery.objects.create(
                name=name,
                email=email,
                company=company,
                phone=phone,
                address1=address1,
                address2=address2,
                address3=address3,
                state=state,
                city=city,
                postalcode=postalcode,
                billing_same=billing_same
            )

            # Clear cart
            cart.clear()

            messages.success(request, f"Congratulations! Your order #{order.order_number} has been placed successfully!")
            return redirect('order_success', order_number=order.order_number)
        else:
            messages.error(request, "Please correct the errors in the delivery form.")
    else:
        form = DeliveryForm()

    return render(request, 'base/deliveryForm.html', {
        'form': form,
        'cart': cart,
        'cart_total': cart.get_total_price(),
    })


def order_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'base/order_success.html', {
        'order': order,
    })


# Contact
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        preference = request.POST.get('preference', '').strip()
        query_type = request.POST.get('querytype', '').strip()
        message = request.POST.get('message', '').strip()

        if first_name and email and message:
            ContactSubmission.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                preference=preference,
                query_type=query_type,
                message=message,
            )
            messages.success(request, 'Thank you! Your message has been submitted successfully. Our team will contact you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'Please complete all required fields.')

    return render(request, 'base/contact.html')
