from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product/images')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
