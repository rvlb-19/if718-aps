from .models import MenuItem

class MenuCollection:
    @staticmethod
    def get_menu():
        return MenuItem.objects.all()

    @staticmethod
    def insert(form):
        return form.save()
