from data import *
import requests
from helper import *


class OrderApi:

    @staticmethod
    def get_id_ingredients():
        url = BASE_URL + INGREDIENTS_URL
        response = requests.get(url)
        response_data = response.json()
        id_ingredients = [item['_id'] for item in response_data['data']]
        return id_ingredients

    @staticmethod
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
    def get_order(access_token):
        url = BASE_URL + USER_ORDER_URL
        header = {'Authorization': access_token}
        response = requests.get(url, headers=header)
        return response




