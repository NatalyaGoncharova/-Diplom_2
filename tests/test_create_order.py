from classes.class_order import *
from data import *


class TestOrderApi:
    def test_create_order_authorised_user_success(self, create_and_delete_user):
        ingredients = OrderApi.get_id_ingredients()[:2]
        email, password, name, response = create_and_delete_user
        access_token = response.json()['accessToken']
        response = OrderApi.create_order(ingredients, access_token)

        assert response.status_code == 200
        assert response.json()['order']['owner']['email'] == email

    def test_create_order_unauthorised_user(self):
        ingredients = OrderApi.get_id_ingredients()[:1]
        response = OrderApi.create_order(ingredients)

        assert response.status_code == 200
        assert response.json()['order']['number'] > 0

    def test_create_order_with_no_ingredients(self, create_and_delete_user):
        ingredients = []
        email, password, name, response = create_and_delete_user
        access_token = response.json()['accessToken']
        response = OrderApi.create_order(ingredients, access_token)

        assert response.status_code == 400
        assert response.json()['message'] == MESSAGE_NO_INGREDIENTS

    def test_create_order_with_wrong_ingredients(self, create_and_delete_user):
        ingredients = ['324re3fdrd3er43erded32']
        response = OrderApi.create_order(ingredients)

        assert response.status_code == 500


