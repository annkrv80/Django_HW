from django.urls import path
from shop_app.views import list_orders, hello

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('client/<int:client_id>/<str:period>', list_orders, name='list_orders'),
]