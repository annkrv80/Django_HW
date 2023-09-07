from django.core.management.base import BaseCommand
from shop_app.models import Order, Client, Product

class Command(BaseCommand):
    help = "Adding a order"

    def handle(self, *args, **kwargs):
        order = Order.objects.create(
            customer = Client.objects.get(pk=5),
            total_price = 0
        )
        order.products.add(Product.objects.get(pk=22))
        order.total_price = sum(product.price for product in order.products.all())
        order.save()
        self.stdout.write(self.style.SUCCESS('Информация успешно добавлена'))