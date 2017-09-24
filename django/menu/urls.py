from django.conf.urls import url
from .controllers import menu_controller, menu_add_controller

urlpatterns = [
    url(r'^$', menu_controller, name='list'),
    url(r'^add/$', menu_add_controller, name='add'),
]
