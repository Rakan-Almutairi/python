from django.contrib import admin

# Register your models here.
from .models import Product, Cat

# Register your models here.
fields = ['image_tag']
readonly_fields = ['image_tag']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price', 'quantity']
    list_filter = ['price']


class CategoryAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name']


admin.site.register(Cat, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
