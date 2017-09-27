from .models import Order, OrderItem

class OrderCollection:
    @staticmethod
    def create(user):
        order = Order(user=user)
        order.save()
        return order

    @staticmethod
    def insert_item(order, item, qnt, price):
        item = OrderItem(order=order, item=item, qnt=qnt, price=price)
        item.save()

    @staticmethod
    def get(id):
        return Order.objects.get(id=id)

    @staticmethod
    def get_order_items(id):
        return OrderCollection.get(i).items()
