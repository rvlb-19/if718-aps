from django.shortcuts import render

from core.facade import Facade
from core.forms import FormFactory

def menu_controller(request):
    return render(request, 'menu/list.html', {
        'menu': Facade.get_menu()
    })

def menu_add_controller(request):
    if request.method == 'POST':
        form = FormFactory.get_instance('menu-add', request.POST)
        response = Facade.add_menu_item(form)
        if response is not None:
            return response
    else:
        form = FormFactory.get_instance('menu-add')
    return render(request, 'menu/add.html', {
        'form': form,
    })
