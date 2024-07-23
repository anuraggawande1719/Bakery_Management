# bakery/views.py

from django.shortcuts import render, redirect
from .models import Product, Customer, Order
from .forms import ProductForm, CustomerForm, OrderForm

def home(request):
    return render(request, "bakery/home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'bakery/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'bakery/add_product.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'bakery/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'bakery/add_customer.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'bakery/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.product.price * order.quantity
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'bakery/add_order.html', {'form': form})
