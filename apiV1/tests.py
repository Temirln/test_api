import pytest

@pytest.mark.django_db
def test_user_add_authenticated(authenticate):
    data = {
        "username":"newUser",
        "email":"newuser@gmail.com",
        "password":"newpassword"
    }

    response = authenticate.post("/api/v1/users/",data)
    assert response.status_code == 201
    
    assert response.data["email"] == data['email']
    assert response.data['username'] == data['username']

@pytest.mark.django_db()
def test_product_add_authenticated(authenticate):
    data = {
        "title":"sugar",
        "price":20
    }

    response = authenticate.post("/api/v1/products/",data)

    assert response.status_code == 201

    assert response.data["title"] == data['title']
    assert int(response.data['price']) == data['price']


@pytest.mark.django_db
def test_order_add_authenticated(authenticate,add_user,add_two_product):
    data = {
        "user":add_user.pk,
        "products":list(add_two_product)
    }
    response = authenticate.post("/api/v1/orders/",data)
    assert response.status_code == 201

    assert response.data["user"] == data['user']
    assert response.data['products'] == data['products']

@pytest.mark.django_db
def test_update_user_athenticated(authenticate,add_user):
    updated_user_data = {
        "username" : "updated user name" 
    }

    response = authenticate.patch(f"/api/v1/user/{add_user.pk}",updated_user_data)
    print(response)
    assert response.status_code == 200

    assert response.data['username'] == updated_user_data['username']


@pytest.mark.django_db
def test_update_product_authenticated(authenticate,add_product):
    updated_product_data = {
        "title" : "updated ice cream" 
    }

    response = authenticate.patch(f"/api/v1/product/{add_product.pk}",updated_product_data)
    print(response)
    assert response.status_code == 200

    assert response.data['title'] == updated_product_data['title']


@pytest.mark.django_db
def test_update_order_athenticated(authenticate,add_order,add_product):
    updated_order_data = {
        "products" : [add_product.pk]
    }

    response = authenticate.patch(f"/api/v1/order/{add_order.pk}",updated_order_data)
    print(response)
    assert response.status_code == 200

    assert response.data['products'] == updated_order_data['products']


@pytest.mark.django_db
def test_delete_user_authenticate(authenticate,add_user):

    response = authenticate.delete(f"/api/v1/user/{add_user.pk}")
    print(response)

    assert response.status_code == 204

@pytest.mark.django_db
def test_delete_order_authenticate(authenticate,add_order):

    response = authenticate.delete(f"/api/v1/order/{add_order.pk}")
    print(response)

    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_product_authenticate(authenticate,add_product):

    response = authenticate.delete(f"/api/v1/product/{add_product.pk}")
    print(response)

    assert response.status_code == 204

# client = Client()

# # class TestGetRequestUserProductOrder(TransactionTestCase):
# # 
#     # @pytest.mark.django_db(transaction=True)
#     # def setUp(self) -> None:
#     #     self.client = APIClient()
#     #     CustomUser.objects.create_user(email="sjdads@jsds",username='testuser', password='testpass')
#     #     CustomUser(email="sjdads@jsds1",username='testuser1', password='testpass').save()

#     #     Product(title="milk",price="10").save()
#     #     Product(title="bread",price="5").save()
        
#     #     # self.client.force_authenticate(user=user)    

# @pytest.mark.django_db(transaction=True)
# def test_get_users():
#     resp = requests.get('http://127.0.0.1:8000/api/v1/users/')
#     assert resp.status_code == 200
#     print(resp.json())

#     first_user = CustomUser.objects.filter().first()
#     assert resp.json()[0]['username'] == first_user.username

# @pytest.mark.django_db(transaction=True)
# def test_get_products():
#     resp = requests.get('http://127.0.0.1:8000/api/v1/products/')
#     assert resp.status_code == 200

#     first_user = Product.objects.filter().first()
#     assert resp.json()[0]['title'] == first_user.title

#     # @pytest.mark.django_db
#     # def test_create_user(self):

#     #     data = {
#     #         "email": "asd@ksj.com",
#     #         "username": "asdsadf",
#     #         "password": "Asdqwwe2124"
#     #     }

#     #     response = self.client.post('http://127.0.0.1:8000/api/v1/users/',data)
#     #     assert response.json()['email'] == "asd@ksj.com"
#     #     assert response.status_code == 201


