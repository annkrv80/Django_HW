from django.core.management.base import BaseCommand
from shop_app.models import Client

class Command(BaseCommand):
    help = "Adding a client"

    def handle(self, *args, **kwargs):
        client = Client(name="Andreev Andrey", email = "andrey@yandex.ru", phoneNumber= '+79601000102',
                adress = "650000, Томск, ул. Мира 1-55")
        client.save()
        self.stdout.write(f'{client}')

    