from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import RegisterForm

class FormFactory:
    '''
    Returns an instance of the requested form, with or
    without data.
    '''
    @staticmethod
    def get_instance(form, data=None):
        if form == 'login':
            return AuthenticationForm(data=data)
        elif form == 'register':
            return RegisterForm(data)
