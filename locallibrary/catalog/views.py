from django.shortcuts import render

# Create your views here.


def home(request):
    title = 'Home Page'
    context = {'title': title}
    return render(request, 'home.html', context)


def product(request, id):
    product_id = id
    title = 'Home Page'
    context = {'title': title, 'product': product_id}
    return render(request, 'home.html', context)


def second_page(request):
    title = 'second Page'
    context = {'title': title}
    return render(request, 'second_page.html', context)
