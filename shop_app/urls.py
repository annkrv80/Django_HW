from django.urls import path
from shop_app.views import list_orders, hello, client_form, product_form, add_client, add_product

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('client/<int:client_id>/<str:period>', list_orders, name='list_orders'),
    path('user/',client_form, name='client_form'),
    path('product/',product_form, name='product_form'),
    path('user/add', add_client, name='add_client'),
    path('product/add', add_product, name='add_product'),
]