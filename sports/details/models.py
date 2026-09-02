from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    department = models.CharField(max_length=100, default='General', help_text="e.g. Football, Running Shoes, Training")
    description = models.TextField(blank=True)
    banner_image = models.CharField(max_length=255, blank=True, default='bg1.png')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return f"{self.department} - {self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.CharField(max_length=100, default='dSports')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    image_name = models.CharField(max_length=255, help_text="Filename in static/css/img/, e.g. RM.jpg")
    available_sizes = models.CharField(max_length=200, default='XS,S,M,L,XL', help_text="Comma-separated sizes (e.g. S,M,L,XL or 8,9,10,11)")
    stock = models.PositiveIntegerField(default=50)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_size_list(self):
        if not self.available_sizes:
            return []
        return [s.strip() for s in self.available_sizes.split(',') if s.strip()]


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    order_number = models.CharField(max_length=50, unique=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=20)
    billing_same = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f"DSP-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} by {self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200)
    image_name = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=20, default='Standard')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product_name} ({self.size})"


class ContactSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preference = models.CharField(max_length=100)
    query_type = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Delivery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=10)
    billing_same = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Delivery to {self.name}, {self.city}"
