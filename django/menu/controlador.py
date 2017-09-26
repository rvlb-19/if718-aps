from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .collection import MenuCollection

class MenuControlador:
    @staticmethod
    def add_menu_item(form):
        if form.is_valid():
            MenuCollection.insert(form)
            return HttpResponseRedirect(reverse_lazy('menu:list'))
        else:
            return None

    @staticmethod
    def get_menu():
        return MenuCollection.get_menu()
