from django.conf.urls import url
from .controllers import (
    login_controller,
    logout_controller,
    signup_controller,
)

urlpatterns = [
    url(r'^login/$', login_controller, name='login'),
    url(r'^logout/$', logout_controller, name='logout'),
    url(r'^register/$', signup_controller, name='register'),
]
