from django.shortcuts import render
from django.views.generic import DetailView

from Products.models import Product


class ProductDetail(DetailView):
    template_name = 'Products/detail.html'
    model = Product
    context_object_name = 'product'
