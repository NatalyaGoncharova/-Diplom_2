from data import *
import requests
import allure


class OrderApi:

    @staticmethod
    @allure.step('Создаем список id ингредиентов')
    def get_id_ingredients():
        url = BASE_URL + INGREDIENTS_URL
        response = requests.get(url)
        response_data = response.json()
        id_ingredients = [item['_id'] for item in response_data['data']]
        return id_ingredients

    @staticmethod
    @allure.step('Создаем заказ с добавлением ингридиентов')
    def create_order(ingredients, access_token=None):
        url = BASE_URL + USER_ORDER_URL
        data = {"ingredients": ingredients}

        if access_token:
            header = {'Authorization': access_token}
            response = requests.post(url, json=data, headers=header)
        else:
            response = requests.post(url, json=data)
        return response

    @staticmethod
    @allure.step('Получаем список заказов авторизованного пользователя')
    def get_order(access_token):
        url = BASE_URL + USER_ORDER_URL
        header = {'Authorization': access_token}
        response = requests.get(url, headers=header)
        return response




