from .models import MenuItem

from core.collection import Collection

class MenuCollection:
    @staticmethod
    def get_menu():
        return Collection(MenuItem).all()

    @staticmethod
    def get(id):
        return Collection(MenuItem).get(id)

    @staticmethod
    def insert(form):
        return Collection(MenuItem).insert(form)
