from typing import Any, Optional
from django.core.management.base import BaseCommand
from shop_app.models import Product

class Command(BaseCommand):
    help = "Adding product in db"

    def handle(self, *args, **kwargs):
        product = Product(name = "Sour cream", description = "A house in the village", price = 74.50, quantity=100) 
        product.save()
        self.stdout.write(f'{product}')


    
    