from .models import User
from django.contrib.auth import authenticate

from core.collection import Collection

class UserCollection:
    @staticmethod
    def verify_user(user):
        return (Collection(User).get(user.id) is not None)

    @staticmethod
    def create_user(form):
        return Collection(User).insert(form)

    @staticmethod
    def retrieve_user(request, email, password):
        return authenticate(request, username=email, password=password)
