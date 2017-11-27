from accounts.models import User
from menu.models import MenuItem

class Collection:
    def __init__(self, cls):
        self.cls = cls

    def insert(self, obj):
        if self.cls in [User, MenuItem]:
            new = obj
        else:
            new = self.cls(**obj)
        new.save()
        return new

    def get(self, id):
        return self.cls.objects.get(id=id)

    def all(self):
        return self.cls.objects.all()
