from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from carton.cart import Cart

from menu.collection import MenuCollection

class OrderControlador:
    @staticmethod
    def cart_action(request, action):
        cart = Cart(request.session)
        item_id = int(request.GET.get('item_id'))
        item = MenuCollection.get(item_id)

        if action == 'add':
            cart.add(item, price=item.price)
            return HttpResponseRedirect(reverse_lazy('menu:list'))
        elif action == 'remove':
            cart.remove(item)
            return HttpResponseRedirect(reverse_lazy('orders:cart'))
