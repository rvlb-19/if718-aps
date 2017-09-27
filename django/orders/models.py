from django.db import models

from menu.models import MenuItem
from accounts.models import User

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    qnt = models.IntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
