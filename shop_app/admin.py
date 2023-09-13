from django.contrib import admin
from shop_app.models import Client, Product, Order
from django.db.models import Sum

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', '-quantity']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phoneNumber']
    list_filter = ['date_regist']
    search_fields = ['name','phoneNumber' ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer', 'date_ordered', 'total_price']
    list_filter = ['customer', 'date_ordered']
    search_fields = ['customer' ]
       
    
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)


