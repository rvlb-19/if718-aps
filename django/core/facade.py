from accounts.controlador import UserControlador
from menu.controlador import MenuControlador
from orders.controlador import OrderControlador

'''
We use this class to access the model layer and perform database operations
'''
class Facade:
    @staticmethod
    def create_user(form):
        return UserControlador.create_user(form)

    @staticmethod
    def log_user_in(request, form):
        return UserControlador.log_user_in(request, form)

    @staticmethod
    def log_user_out(request):
        return UserControlador.log_user_out(request)

    @staticmethod
    def user_is_authenticated(request):
        return UserControlador.user_is_authenticated(request)

    @staticmethod
    def add_menu_item(form):
        return MenuControlador.add_menu_item(form)

    @staticmethod
    def get_menu():
        return MenuControlador.get_menu()

    @staticmethod
    def cart_action(request, action):
        return OrderControlador.cart_action(request, action)

    @staticmethod
    def finalize_order(request):
        return OrderControlador.finalize_order(request)
