from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.ulogin, name='login'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]