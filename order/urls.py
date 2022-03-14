from django.urls import path, include
from django.views.generic.base import View

from order import views


app_name = 'order'
urlpatterns = [
    path('list/', views.OrdersListView.as_view(), name='order_list'),
]
