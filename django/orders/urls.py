from django.conf.urls import url
from .controllers import (
    cart_controller,
    add_to_cart_controller,
    remove_from_cart_controller,
)

urlpatterns = [
    url(r'^cart/$', cart_controller, name='cart'),
    url(r'^cart/add/$', add_to_cart_controller, name='add_cart'),
    url(r'^cart/remove/$', remove_from_cart_controller, name='remove_cart'),
]
