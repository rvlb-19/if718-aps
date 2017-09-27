from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from accounts.decorators import auth_decorator
from core.facade import Facade

def cart_controller(request):
    return render(request, 'orders/cart.html', {})

def add_to_cart_controller(request):
    return Facade.cart_action(request, 'add')

def remove_from_cart_controller(request):
    return Facade.cart_action(request, 'remove')

@auth_decorator(lambda x: x, url=reverse_lazy('accounts:login'))
def finalize_order_controller(request):
    return Facade.finalize_order(request)
