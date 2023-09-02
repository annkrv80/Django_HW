from decimal import Decimal
from django.core.management.base import BaseCommand, CommandParser
from shop_app.models import Product

class Command(BaseCommand):
    help = "Product price change"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product_Id')
        parser.add_argument('price', type=Decimal, help='New price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.price=new_price
        product.save()
        self.stdout.write(f'{product}')
