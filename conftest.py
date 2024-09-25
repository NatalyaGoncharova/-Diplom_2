import pytest
from faker import Faker
from classes.class_user import *

fake = Faker()


@pytest.fixture
def create_and_delete_user():
    email = fake.email()
    password = fake.password()
    name = fake.name()
    response = UserApi.registrate_user(email, password, name)
    access_token = response.json()['accessToken']
    yield email, password, name, response
    UserApi.delete_user(access_token)


@pytest.fixture
def login_and_logout_user(create_and_delete_user):
    email, password, name, response = create_and_delete_user
    refresh_token = response.json()['refreshToken']
    response_login = UserApi.login_user(email, password)
    yield response_login, email, password
    UserApi.logout_user(refresh_token)