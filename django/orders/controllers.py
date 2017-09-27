from django.shortcuts import render
from django.contrib import messages

from core.facade import Facade

def cart_controller(request):
    return render(request, 'orders/cart.html', {})

def add_to_cart_controller(request):
    messages.success(request, 'Item adicionado ao carrinho!')
    return Facade.cart_action(request, 'add')

def remove_from_cart_controller(request):
    return Facade.cart_action(request, 'remove')
