from .models import Order, OrderItem
from core.collection import Collection

class OrderCollection:
    @staticmethod
    def create(user):
        c = Collection(Order)
        return c.insert({ 'user': user })

    @staticmethod
    def insert_item(order, item, qnt, price):
        c = Collection(OrderItem)
        c.insert({ 'order': order, 'item': item, 'qnt': qnt, 'price': price })

    @staticmethod
    def get(id):
        return Collection(Order).get(id)

    @staticmethod
    def get_order_items(id):
        return OrderCollection.get(id).items()
