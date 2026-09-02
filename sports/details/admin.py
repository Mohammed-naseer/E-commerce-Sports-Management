from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ContactSubmission, Delivery

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'department')
    list_filter = ('department',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'original_price', 'stock', 'is_featured', 'created_at')
    list_filter = ('category', 'brand', 'is_featured', 'created_at')
    search_fields = ('name', 'description', 'brand')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'is_featured')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product_name', 'price', 'quantity', 'size', 'total_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'email', 'phone', 'city', 'state', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'state', 'created_at')
    search_fields = ('order_number', 'name', 'email', 'phone', 'address1')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    readonly_fields = ('order_number', 'created_at')

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'query_type', 'preference', 'submitted_at')
    list_filter = ('query_type', 'preference', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'message')
    readonly_fields = ('submitted_at',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'state', 'postalcode', 'created_at')
    search_fields = ('name', 'email', 'phone', 'city', 'state')
    readonly_fields = ('created_at',)
