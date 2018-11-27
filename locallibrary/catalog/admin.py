from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'quantity']
    list_filter = ['price']


class CategoryAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


