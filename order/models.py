from django.db import models

from accounts.models import User
from store.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cartitem')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitem')
    quantity = models.IntegerField(default=0, blank=True, null=True)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.item.name


class Order(models.Model):
    PAYMENT_METHOD = (
    ('cash', 'Cash On Delivery'),
    ('paypal', 'PayPal'),
    )

    ORDER_STATUS = (
        ('pending', 'pending'),
        ('proccessing', 'proccessing'),
        ('complete', 'complete'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    cartitems = models.ManyToManyField(CartItem)
    ordered = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=ORDER_STATUS, default='pending')
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD, default="Cash On Delivery")
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    orderId = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


