import pytest

from apiV1.models import CustomUser
from apiV1.models import Order, Product
from  rest_framework.test import APIClient

@pytest.fixture
def authenticate():
    user = CustomUser.objects.create_user(email = "test@gmail.com",username = "testname",password = "testpassword")
    client = APIClient()
    client.force_login(user)

    return client

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def add_user():
    return CustomUser.objects.create_user(email = "newUser@gmail.com",username = "newname",password = "newpassword")
    


@pytest.fixture
def add_order():
    new_user = CustomUser.objects.create_user(email = "orderUser@gmail.com",username = "ordername",password = "orderpassword")
    product = Product.objects.create(title = "sugar",price = 14)

    order = Order.objects.create(user = new_user)
    order.products.add(product)
    order.save()
    return order

@pytest.fixture
def add_two_product():
    product1 = Product(title = "milk",price = "10")
    product2 = Product(title = "bread",price = "5")
    product1.save()
    product2.save()
    return product1.pk,product2.pk

@pytest.fixture
def add_product():
    product = Product(title = "ice cream",price = "5")
    product.save()
    return product
