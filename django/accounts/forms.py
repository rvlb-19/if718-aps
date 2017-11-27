from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)
        instance.username = instance.email
        if commit:
            instance.save()
        return instance
