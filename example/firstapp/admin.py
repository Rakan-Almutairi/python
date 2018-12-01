from django.contrib import admin

# Register your models here.
from .models import Car, CarType


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['name', 'price', 'quantity', 'image']
    list_filter = ['price']


class CarTypeAdmin(admin.ModelAdmin):
    model = CarType
    list_display = ['name']


admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
