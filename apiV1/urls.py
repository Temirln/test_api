from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("users/", views.UsersApiGeneric.as_view(), name="users"),
    path("user/<int:pk>",views.UsersDetail.as_view(), name="user_detail"),

    path("orders/", views.OrdersApiGeneric.as_view(), name="orders"),
    path("order/<int:pk>",views.OrdersDetail.as_view(), name="order_detail"),

    path("products/", views.ProductsApiGeneric.as_view(), name="products"),
    path("product/<int:pk>",views.ProductsDetail.as_view(), name="product_detail"),
]