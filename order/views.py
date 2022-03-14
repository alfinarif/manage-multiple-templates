from django.shortcuts import render

from order.models import CartItem, Order
from store.models import Product

from django.views.generic import ListView



class OrdersListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'dashboard/orders_list.html'

