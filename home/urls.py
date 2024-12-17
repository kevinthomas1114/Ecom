from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.ulogin, name='login'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart')
]
