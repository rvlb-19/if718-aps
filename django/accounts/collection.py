from .models import User
from django.contrib.auth import authenticate

class UserCollection:
    @staticmethod
    def verify_user(user):
        return (User.objects.get(id=user.id) is not None)

    @staticmethod
    def create_user(form):
        return form.save()

    @staticmethod
    def retrieve_user(request, email, password):
        return authenticate(request, username=email, password=password)
