import pytest
from faker import Faker
from classes.class_user import UserApi
from data import *

fake = Faker()


class TestUserChangeDataApi:
    @pytest.mark.parametrize("field,value", [('email', fake.email()),
                                             ('password', fake.password()),
                                             ('name', fake.name())])
    def test_change_user_data_success(self, create_and_delete_user, field, value):
        email, password, name, response = create_and_delete_user
        access_token = response.json()['accessToken']
        data = {"email": email, "password": password, "name": name}
        data[field] = value
        response_change = UserApi.change_user_data(data['email'], data['password'], data['name'], access_token)

        assert response_change.status_code == 200
        assert response_change.json()['success'] == True

    def test_change_data_no_authorized_user(self, create_and_delete_user):
        email, password, name, response = create_and_delete_user
        access_token = fake.password()
        response_change = UserApi.change_user_data(email, password, name, access_token)

        assert response_change.status_code == 401
        assert response_change.json()['message'] == MESSAGE_NO_AUTHORIZATION

