from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    adress = models.CharField(max_length=200)
    date_regist = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='media/')

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Заказ {self.pk} от {self.date_ordered} для {self.customer}'