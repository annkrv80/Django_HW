from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from shop_app.models import Client, Product, Order
from datetime import timedelta
from django.utils import timezone

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
    
