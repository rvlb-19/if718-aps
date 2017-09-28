from django.db import models

class MenuItem(models.Model):
    name = models.CharField('Nome do Item', max_length=200)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
