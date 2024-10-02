from classes.class_user import UserApi
from data import *
from faker import Faker
import allure
fake = Faker()


class TestLogUserApi:
    @allure.title("Авторизация с корректными данными")
    def test_login_user_correct_data_success(self, login_and_logout_user):
        response_login, email, password = login_and_logout_user

        assert email == response_login.json()['user']['email']
        assert 200 == response_login.status_code

    @allure.title("Авторизация с данными не зарегистрированного пользователя")
    def test_login_user_incorrect_data(self):
        email = fake.email()
        password = fake.password()
        response = UserApi.login_user(email, password)

        assert 401 == response.status_code
        assert response.json()['message'] == MESSAGE_INCORRECT_LOGIN_DATA



