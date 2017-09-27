from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

def auth_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, url=None):
    return user_passes_test(
        lambda u: u.is_authenticated,
        login_url=url,
        redirect_field_name=redirect_field_name
    )

def no_authentication(function=None, redirect_field_name=REDIRECT_FIELD_NAME, url=None):
    return user_passes_test(
        lambda u: (not u.is_authenticated),
        login_url=url,
        redirect_field_name=redirect_field_name
    )
