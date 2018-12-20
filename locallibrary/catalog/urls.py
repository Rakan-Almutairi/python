from django.urls import path
from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'product/<int:id>/', views.product, name='product'),
    path(r'products/', views.products, name='products'),
    path(r'add-products/', views.add_product, name='add-products'),
    path('page-number-2/', views.second_page, name='second-page')
]

