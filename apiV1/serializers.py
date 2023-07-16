from rest_framework import serializers

from .models import CustomUser, Order, Product

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email','username','password']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"    


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"