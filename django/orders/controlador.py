from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

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
            messages.success(request, '{} adicionado ao carrinho!'.format(item.name))
            return HttpResponseRedirect(reverse_lazy('menu:list'))
        elif action == 'remove':
            cart.remove(item)
            messages.success(request, '{} removido do carrinho!'.format(item.name))
            return HttpResponseRedirect(reverse_lazy('orders:cart'))

    @staticmethod
    def finalize_order(request):
        cart = Cart(request.session)
        if not cart.items:
            return HttpResponseRedirect(reverse_lazy('orders:cart'))
        cart.clear()
        messages.success(request, 'Pedido realizado com sucesso!')
        return HttpResponseRedirect(reverse_lazy('core:index'))
