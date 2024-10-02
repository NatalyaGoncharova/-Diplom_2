from classes.class_user import UserApi
from faker import Faker
from data import *
import allure

fake = Faker()


class TestUserApi:
    @allure.title("Регистрация пользователя с валидными параметрами")
    def test_registration_user_success(self, create_and_delete_user):
        email, password, name, response = create_and_delete_user

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title("Регистрация пользователя с уже зарегистрированным email")
    def test_registration_existed_user_impossible(self, create_and_delete_user):
        email, password, name, response = create_and_delete_user
        response = UserApi.registrate_user(email, password, name)

        assert response.status_code == 403
        assert response.json()['message'] == MESSAGE_USER_EXIST

    @allure.title("Регистрация пользователя без указания email")
    def test_registration_user_with_empty_email_impossible(self):
        email = ''
        password = fake.password()
        name = fake.name()
        response = UserApi.registrate_user(email, password, name)

        assert response.status_code == 403
        assert response.json()['message'] == MESSAGE_USER_REQUIRED_DATA



