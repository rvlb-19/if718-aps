from django.forms import ModelForm
from .models import MenuItem

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
