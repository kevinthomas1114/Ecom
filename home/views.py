from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
def home(request):
    product=Product.objects.all()
    return render(request,'home.html',{'product':product})
def ulogin(request):
    error_message = ""  
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        print(f"Attempting login for Username: {username}, Password: {password}")
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            print("Authentication failed!")
            error_message = "Invalid Username or Password"
    return render(request, 'ulogin.html', {'error_message': error_message})

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    total = 0
    for item in cart_items:
        item.subtotal = item.quantity * item.products.price
        total += item.subtotal  
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, products=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
