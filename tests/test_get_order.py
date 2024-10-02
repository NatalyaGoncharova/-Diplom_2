from classes.class_order import *
from data import *


class TestOrderApiGet:
    @allure.title("Получение заказа авторизованного пользователя")
    def test_get_order_authorized_user_success(self, create_and_delete_user):
        ingredients = OrderApi.get_id_ingredients()[:2]
        email, password, name, response = create_and_delete_user
        access_token = response.json()['accessToken']
        OrderApi.create_order(ingredients, access_token)
        response = OrderApi.get_order(access_token)

        assert response.status_code == 200

        order = response.json()['orders'][0]
        order_ingredients = order['ingredients']

        assert order_ingredients == ingredients

    @allure.title("Получение заказа без указания access_token")
    def test_get_order_unauthorized_user(self):
        access_token = ''
        response = OrderApi.get_order(access_token)

        assert response.status_code == 401
        assert response.json()['message'] == MESSAGE_NO_AUTHORIZATION
