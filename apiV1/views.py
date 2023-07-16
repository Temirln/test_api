from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from .serializers import OrdersSerializer, ProductsSerializer, UsersSerializer
from . import models

# Create your views here.

class UsersApiGeneric(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UsersSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UsersSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ProductsApiGeneric(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductsSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductsSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





class OrdersApiGeneric(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = OrdersSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = OrdersSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
