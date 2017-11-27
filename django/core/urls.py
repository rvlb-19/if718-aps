from django.conf.urls import url
from .controllers import index_controller

urlpatterns = [
    url(r'^$', index_controller, name='index'),
]
