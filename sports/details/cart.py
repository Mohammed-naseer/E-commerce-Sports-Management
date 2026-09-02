from decimal import Decimal
from django.conf import settings
from .models import Product

class Cart:
    def __init__(self, request):
        """
        Initialize the shopping cart using session.
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def _get_item_key(self, product_id, size):
        return f"{product_id}_{size}"

    def add(self, product, size='Standard', quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        item_key = self._get_item_key(product_id, size)

        if item_key not in self.cart:
            self.cart[item_key] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'image_name': product.image_name,
                'size': size,
                'quantity': 0,
            }

        if override_quantity:
            self.cart[item_key]['quantity'] = max(1, int(quantity))
        else:
            self.cart[item_key]['quantity'] += int(quantity)

        self.save()

    def remove(self, product_id, size='Standard'):
        """
        Remove a product from the cart.
        """
        item_key = self._get_item_key(product_id, size)
        if item_key in self.cart:
            del self.cart[item_key]
            self.save()

    def update_quantity(self, product_id, size, quantity):
        """
        Update quantity of an item directly.
        """
        item_key = self._get_item_key(product_id, size)
        if item_key in self.cart:
            qty = int(quantity)
            if qty > 0:
                self.cart[item_key]['quantity'] = qty
            else:
                del self.cart[item_key]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = [item['product_id'] for item in self.cart.values()]
        products = Product.objects.filter(id__in=product_ids)
        product_map = {p.id: p for p in products}

        for item_key, item in self.cart.items():
            item_copy = item.copy()
            item_copy['item_key'] = item_key
            item_copy['price'] = Decimal(item['price'])
            item_copy['total_price'] = item_copy['price'] * item_copy['quantity']
            item_copy['product'] = product_map.get(item['product_id'])
            yield item_copy

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove cart from session.
        """
        del self.session['cart']
        self.save()
