from Products.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['upk'] = self.unicque_id_generator(product.id, item['size'], item['color'])
            yield item

    def unicque_id_generator(self, id, size, color):
        result = f'{id}-{size}-{color}'

        return result

    def add(self, product, quantity, color, size):
        unique_id = self.unicque_id_generator(id=product.id, size=size, color=color)
        if unique_id not in self.cart:
            self.cart[unique_id] = {'quantity': 1, 'price': str(product.price), 'size': size, 'color': color,
                                    'id': product.id}
        self.cart[unique_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session.modified = True

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()
