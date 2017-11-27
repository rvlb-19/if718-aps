from accounts.models import User
from menu.models import MenuItem

class Collection:
    def __init__(self, cls):
        self.cls = cls
        self.objects = self.cls.objects

    def insert(self, obj):
        if self.cls in [User, MenuItem]:
            new = obj
        else:
            new = self.cls(**obj)
        new.save()
        self.objects = self.cls.objects
        return new

    def get(self, id):
        return self.objects.get(id=id)

    def all(self):
        return self.objects.all()
