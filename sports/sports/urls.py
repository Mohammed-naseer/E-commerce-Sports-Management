"""
URL configuration for sports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from details import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cart/', views.cart,name='cart'),
    path('contact/',views.contact,name='contact'),
    path('jersey/',views.jersey,name='jersey'),
    path('shoes/',views.shoes,name='shoes'),
    path('accessories/',views.accessories,name='accessories'),
    path('delivery/',views.deliveryForm,name='deliveryForm'),
    path('femaleRunningShoes/',views.femaleRunningShoes,name='femaleRunningShoes'),
    path('maleRunningShoes/',views.maleRunningShoes,name='maleRunningShoes'),
    path('trainingKids/', views.trainingKids, name='trainingkids'),
 
    path('trainingmen/',views.trainingmen,name='trainingmen'),
    path('trainingwomen/',views.trainingwomen,name='trainingwomen'),
]
