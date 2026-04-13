from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm

def index(request):
    products = Products.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def add_product(request):
    # Nếu là POST: kiểm tra form.is_valid(), đúng thì lưu database
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_success')
    else:
        # GET: trả về 1 form trống
        form = ProductForm()
    
    return render(request, 'shop/add_product.html', {'form': form})

def product_success(request):
    return render(request, 'shop/product_success.html')
