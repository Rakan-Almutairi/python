from django.db import models

# Create your models here.

# class user(models.Model):
#     first_name = models.CharField(max_length=50)
#     middile_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#
#
#     @property
#     def fullname(self):
#         return self.first_name + self.middile_name + self.last_name


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     parents = models.ManyToManyField('self', 'children', symmetrical=False, blank=True)
#
#     @property
#     def parent(self):
#         allcats = [cat for cat in self.parents.values_list('name', flat=True)]
#         return ', '.join(allcats)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product/images', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
