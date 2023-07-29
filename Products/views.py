from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product


class ProductDetail(DetailView):
    template_name = 'Products/detail.html'
    model = Product
    context_object_name = 'product'


class ProductList(ListView):
    template_name = 'Products/productlist.html'
    model = Product
    paginate_by = 1
    context_object_name = 'productlist'
    queryset = Product.objects.order_by('title')

