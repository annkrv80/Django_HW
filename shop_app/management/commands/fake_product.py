from random import choices
from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from shop_app.models import Product

products =['Sugar', 'Coffee', 'Tea', 'Pasta', 'Rice','Salt',\
            'Buckwheat', 'Strawberry', 'Chocolate', 'Pear', 'Grapes', 'Candy', 'Egg', 'Fish', 'Cheese']

class Command(BaseCommand):
    help = "Generate fake product"


    def handle(self, *args, **kwargs):    
        for item in products:
            product = Product(name = item, description = f"The best {item}", price = 50.50,\
                            quantity=100) 
            product.save()