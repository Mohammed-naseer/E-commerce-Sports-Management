from .cart import Cart
from .models import Category

def sports_context(request):
    cart = Cart(request)
    categories = Category.objects.all()
    return {
        'cart': cart,
        'cart_count': len(cart),
        'cart_total': cart.get_total_price(),
        'all_categories': categories,
    }
