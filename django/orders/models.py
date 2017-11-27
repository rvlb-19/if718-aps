from django.db import models

from menu.models import MenuItem
from accounts.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def items(self):
        return self.orderitem_set.all()

    def total(self):
        price = 0
        for i in self.items():
            price += i.subtotal()
        return price

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    qnt = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço pago', max_digits=100, decimal_places=2)

    def subtotal(self):
        return self.qnt*self.price
