from rest_framework import fields, serializers

from order.models import Order, CartItem
from store.models import Product, Category, Brand
from notification.models import OrderNotification

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'is_admin',
        )



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'parent',
            'name',
            'image',
            
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'image',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'brand',
            'preview_des',
            'description',
            'image',
            'price',
            'old_price',
            'is_stock',
        )
    
    def get_category(self, obj):
        return CategorySerializer(obj.category).data

    def get_brand(self, obj):
        return BrandSerializer(obj.brand).data


class CartItemsSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = (
            'item',
            'quantity',
            'purchased',
            )

    def get_item(self, obj):
        return ProductSerializer(obj.item).data


class OrderListSerializer(serializers.ModelSerializer):
    cartitems = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'cartitems',
            'ordered',
            'status',
            'payment_method',
            'created',
        )
    
    def get_cartitems(self, obj):
        return CartItemsSerializer(obj.cartitems.all(), many=True).data
    
    def get_user(self, obj):
        return UserSerializer(obj.user).data





class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderNotification
        fields = ('__all__')

