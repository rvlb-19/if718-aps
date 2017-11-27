from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from .collection import MenuCollection

class MenuControlador:
    @staticmethod
    def add_menu_item(request, form):
        if form.is_valid():
            MenuCollection.insert(form)
            messages.success(request, 'Item adicionado com sucesso!')
            return HttpResponseRedirect(reverse_lazy('menu:list'))
        else:
            return None

    @staticmethod
    def get_menu():
        return MenuCollection.get_menu()
