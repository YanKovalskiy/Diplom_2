# Создание пользователя:
# --------------------------------------------------------------
# создать уникального пользователя;
# создать пользователя, который уже зарегистрирован;
# создать пользователя и не заполнить одно из обязательных полей.

import allure
import pytest


class TestCreateUser:

    @allure.title('Создание уникального пользователя позитивный сценарий')
    def test_create_unique_user(self, user_endpoints, payload_for_create_user):
        user_endpoints.create_user(payload_for_create_user)

        user_endpoints.check_status_code_is_(200)
        user_endpoints.check_response_field('success', True)

        headers = {"Authorization": user_endpoints.get_access_token()}
        user_endpoints.delete_user(headers)

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_already_registered_user(self, new_user, user_endpoints, payload_for_create_user):
        user_endpoints.create_user(payload_for_create_user)
        user_endpoints.check_status_code_is_(403)
        user_endpoints.check_response_field('success', False)
        user_endpoints.check_response_field('message', 'User already exists')

    @allure.title('Создание пользователя, не заполняя одно из обязательных полей')
    @pytest.mark.parametrize(
        'required_field',
        ('email', 'password', 'name')
    )
    def test_create_user_without_fill_one_of_required_fields(self, user_endpoints,
                                                             payload_for_create_user, required_field):
        payload_for_create_user[required_field] = ''
        user_endpoints.create_user(payload_for_create_user)
        user_endpoints.check_status_code_is_(403)
        user_endpoints.check_response_field('success', False)
        user_endpoints.check_response_field('message', 'Email, password and name are required fields')
