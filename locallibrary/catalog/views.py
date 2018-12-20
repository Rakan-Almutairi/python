from django.shortcuts import render

from catalog.forms import ProductForm
from .models import Product


# Create your views here.


def home(request):
    title = 'Home Page'
    context = {'title': title}
    return render(request, 'home.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product(request, id):
    product = Product.objects.filter(id=id)
    title = 'Home Page'
    context = {'title': title, 'product': product}
    return render(request, 'home.html', context)


def second_page(request):
    title = 'second Page'
    context = {'title': title}
    return render(request, 'second_page.html', context)


def add_product(request):
    product = Product.objects.get(id=5)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid:
            print(form.errors)
            instance = form.save(commit=False)
            instance.quantity = 90
            instance.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)

def edit_product(request, id):
    product = Product.objects.get(id=5)
    form = ProductForm(instance= product)
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid:
            print(form.errors)
            instance = form.save(commit=False)
            instance.quantity = 90
            instance.save()
        print("this is post page")
    context = {'form': form}
    return render(request, 'add-product.html', context)