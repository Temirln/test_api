from apiV1.models import CustomUser, Product
import requests
import pytest
from  rest_framework.test import APIClient
from django.test import Client,TestCase,TransactionTestCase
import logging
LOGGER = logging.getLogger(__name__)


client = Client()

# class TestGetRequestUserProductOrder(TransactionTestCase):
# 
    # @pytest.mark.django_db(transaction=True)
    # def setUp(self) -> None:
    #     self.client = APIClient()
    #     CustomUser.objects.create_user(email="sjdads@jsds",username='testuser', password='testpass')
    #     CustomUser(email="sjdads@jsds1",username='testuser1', password='testpass').save()

    #     Product(title="milk",price="10").save()
    #     Product(title="bread",price="5").save()
        
    #     # self.client.force_authenticate(user=user)    

@pytest.mark.django_db(transaction=True)
def test_get_users():
    resp = requests.get('http://127.0.0.1:8000/api/v1/users/')
    assert resp.status_code == 200
    print(resp.json())

    first_user = CustomUser.objects.filter().first()
    assert resp.json()[0]['username'] == first_user.username

@pytest.mark.django_db(transaction=True)
def test_get_products():
    resp = requests.get('http://127.0.0.1:8000/api/v1/products/')
    assert resp.status_code == 200

    first_user = Product.objects.filter().first()
    assert resp.json()[0]['title'] == first_user.title

    # @pytest.mark.django_db
    # def test_create_user(self):

    #     data = {
    #         "email": "asd@ksj.com",
    #         "username": "asdsadf",
    #         "password": "Asdqwwe2124"
    #     }

    #     response = self.client.post('http://127.0.0.1:8000/api/v1/users/',data)
    #     assert response.json()['email'] == "asd@ksj.com"
    #     assert response.status_code == 201


