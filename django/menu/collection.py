from .models import MenuItem

class MenuCollection:
    @staticmethod
    def get_menu():
        return MenuItem.objects.all()

    @staticmethod
    def get(id):
        return MenuItem.objects.get(id=id)

    @staticmethod
    def insert(form):
        return form.save()
