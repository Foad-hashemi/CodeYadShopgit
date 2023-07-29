from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import View

from Order.cart import Cart
from Products.models import Product


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        context = 0
        for item in request.session['cart'].values():
            context += item['quantity'] * int(item['price'])
        return render(self.request, 'Orders/cart.html', {'cart': cart, 'total': context})


class CartHandelView(View):
    def post(self, request, pk):
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        product = get_object_or_404(Product, id=pk)
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect('Order:cart')


class CartDeleteItem(View):
    def get(self, request, upk):
        cart = Cart(request)
        cart.delete(upk)
        return redirect('Order:cart')

