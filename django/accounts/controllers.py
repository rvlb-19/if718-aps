from .models import User

from core.facade import Facade
from core.forms import FormFactory

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

def signup_controller(request):
    '''
    1. If we are accessing the view using POST, it means we are sending
    a request to the controller to save data. We acquire the form through
    factory and pass the POST data to it. With the retrieved info, we access
    the model layer through the facade and request the creation of an user.
    2. If the request is not made via POST, we will simply render an empty form.
    '''
    if request.method == 'POST':
        form = FormFactory.get_instance('register', request.POST)
        response = Facade.create_user(request, form)
        if response is not None:
            return response
    else:
        form = FormFactory.get_instance('register')
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login_controller(request):
    if Facade.user_is_authenticated(request):
        return HttpResponseRedirect(reverse_lazy('core:index'))

    if request.method == 'POST':
        form = FormFactory.get_instance('login', request.POST)
        response = Facade.log_user_in(request, form)
        if response is not None:
            return response
    else:
        form = FormFactory.get_instance('login')
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout_controller(request):
    return Facade.log_user_out(request)

def order_history_controller(request):
    if not Facade.user_is_authenticated(request):
        return HttpResponseRedirect(reverse_lazy('core:index'))

    return render(request, 'accounts/orders.html', {
        'list': Facade.order_history(request)
    })
