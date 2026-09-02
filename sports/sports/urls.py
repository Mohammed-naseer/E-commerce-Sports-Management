from django.contrib import admin
from django.urls import path
from details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    # Shop & Categories
    path('shop/', views.product_list, name='shop'),
    path('shop/<slug:category_slug>/', views.product_list, name='category_products'),
    path('jersey/', views.jersey, name='jersey'),
    path('shoes/', views.shoes, name='shoes'),
    path('accessories/', views.accessories, name='accessories'),
    path('femaleRunningShoes/', views.femaleRunningShoes, name='femaleRunningShoes'),
    path('maleRunningShoes/', views.maleRunningShoes, name='maleRunningShoes'),
    path('trainingKids/', views.trainingKids, name='trainingkids'),
    path('trainingmen/', views.trainingmen, name='trainingmen'),
    path('trainingwomen/', views.trainingwomen, name='trainingwomen'),

    # Cart URLs
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/update/', views.cart_update, name='cart_update'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),

    # Delivery & Checkout
    path('delivery/', views.deliveryForm, name='deliveryForm'),
    path('checkout/', views.deliveryForm, name='checkout'),
    path('order-success/<str:order_number>/', views.order_success, name='order_success'),

    # Contact
    path('contact/', views.contact, name='contact'),
]
