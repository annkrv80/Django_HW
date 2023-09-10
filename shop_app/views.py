from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from shop_app.models import Client, Product, Order
from datetime import timedelta
from django.utils import timezone
from .forms import ClientForm, ProductForm
import logging


logger = logging.getLogger(__name__)

def hello(request):
    return HttpResponse("Hello!")


def list_orders (request, client_id, period):
    client = get_object_or_404(Client, pk=client_id)
    products_set = set()

    if period == 'week':
        week = timezone.now() - timedelta(days=7)  
        week_orders = Order.objects.filter(customer=client, date_ordered__gte=week)
        for order in week_orders:
            products_set.update(order.products.all())
    elif period == 'month':
        month = timezone.now() - timedelta(days=30) 
        month_orders = Order.objects.filter(customer=client, date_ordered__gte=month)
        for order in month_orders:
            products_set.update(order.products.all())
    elif period == 'year':
        year = timezone.now() - timedelta(days=365)
        year_orders = Order.objects.filter(customer=client, date_ordered__gte=year)
        for order in year_orders:
            products_set.update(order.products.all())
    context = {'client': client, 'period': period, 'products': products_set}

    return render(request, 'shop_app/list_orders.html', context )   
    
def client_form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phoneNumber']
            adress = form.cleaned_data['adress']
            date_regist = form.cleaned_data['date_regist']
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ClientForm()
    return render(request, 'shop_app/client_form.html', {'form':form})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.changed_data['price']
            quantity = form.cleaned_data['quantity']            
            date_add = form.cleaned_data['date_add']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)           
    else:
        form = ProductForm
    return render(request, 'shop_app/product_form.html', {'form':form})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneNumber = form.cleaned_data['phoneNumber']
            adress = form.cleaned_data['adress']
            date_regist = form.cleaned_data['date_regist']
            logger.info(f'Получили {form.cleaned_data=}.')
            client = Client(name=name, email = email, phoneNumber= phoneNumber,
                adress = adress, date_regist=date_regist)
            client.save()
            message = 'Пользователь сохранён'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'shop_app/client_form.html', {'form': form, 'message': message})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_add = form.cleaned_data['date_add']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image) 
            product = Product(name = name, description = description, price = price, quantity=quantity,
                               date_add=date_add, image=image) 
            product.save()
            message = 'Пользователь сохранён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'shop_app/product_form.html', {'form': form, 'message': message})
