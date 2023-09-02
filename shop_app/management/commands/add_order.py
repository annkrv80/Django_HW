from django.core.management.base import BaseCommand
from shop_app.models import Order, Client, Product

class Command(BaseCommand):
    help = "Adding a order"

    def handle(self, *args, **kwargs):
        order = Order.objects.create(
            customer=Client.objects.get(pk=1),
            total_price=99.99,
        )
        order.products.add(Product.objects.get(pk=1))
        self.stdout.write(self.style.SUCCESS('Информация успешно добавлена'))