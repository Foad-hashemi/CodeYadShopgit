from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    pass


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Color(models.Model):
    color = models.CharField(max_length=10, editable=True)

    def __str__(self):
        return self.color


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size, blank=True, null=True)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return self.title


class Information(models.Model):
    text = RichTextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='info')
