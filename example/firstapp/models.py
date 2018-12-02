from django.db import models


# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product/images')
    CarType = models.ForeignKey('CarType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
