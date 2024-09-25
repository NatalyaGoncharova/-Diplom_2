from data import *
import requests
from helper import *


class UserApi:
    @staticmethod
    def registrate_user(email, password, name):
        url = BASE_URL + REGISTRATION_URL
        data = UserData.get_user_registration_data(email, password, name)
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def delete_user(access_token):
        url = BASE_URL + USER_DATA_URL
        header = {'Authorization': f'Bearer {access_token}'}
        response = requests.delete(url, headers=header)
        return response

    @staticmethod
    def login_user(email, password):
        url = BASE_URL + AUTHORISATION_URL
        data = UserData.get_user_login_data(email, password)
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def logout_user(refresh_token):
        url = BASE_URL + LOGOUT_URL
        data = UserData.get_user_logout_data(refresh_token)
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def change_user_data(email, password, name, access_token):
        url = BASE_URL + USER_DATA_URL
        data = UserData.get_user_registration_data(email, password, name)
        header ={'Authorization': access_token}
        response = requests.patch(url, json=data, headers=header)
        return response

