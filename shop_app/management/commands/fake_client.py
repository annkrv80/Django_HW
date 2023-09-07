from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from shop_app.models import Client
from datetime import datetime

class Command(BaseCommand):
    help = "Generate fake client."

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Client_ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in  range(count + 1):
            client = Client(name=f"Test_{i} Testo_{i}", email = f"mail_{i}@yandex.ru", phoneNumber= f'+79601000100+{i}',
                adress = f"65000{i}, City_{i}, ул. Мира {i}-{i+1}")
            client.save()