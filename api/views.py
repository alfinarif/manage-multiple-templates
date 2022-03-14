from django.shortcuts import render

from order.models import CartItem, Order
from store.models import Product

from rest_framework.decorators import api_view, permission_classes

from rest_framework import permissions
from rest_framework import response, viewsets

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.serializers import (
    OrderListSerializer, 
    ProductSerializer, 
    NotificationSerializer
    )


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


    
class OrderListApiView(ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(ordered=True)



class OrderNotificationApiView(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return OrderNotification.objects.filter(is_read=False)
