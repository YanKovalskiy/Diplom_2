import allure
import pytest


class TestCreateUser:

    @allure.title('Создание уникального пользователя позитивный сценарий')
    def test_create_unique_user(self, user_endpoints, payload_for_create_user):
        user_endpoints.create_user(payload_for_create_user)
        user_endpoints.check_status_code_is_(200)
        user_endpoints.check_response_field_success_is_(True)

        headers = {"Authorization": user_endpoints.access_token}
        user_endpoints.delete_user(headers)

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_already_registered_user(self, new_user, user_endpoints, payload_for_create_user):
        user_endpoints.create_user(payload_for_create_user)
        user_endpoints.check_status_code_is_(403)
        user_endpoints.check_response_field_success_is_(False)
        user_endpoints.check_response_field_message_is_('User already exists')

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
        user_endpoints.check_response_field_success_is_(False)
        user_endpoints.check_response_field_message_is_('Email, password and name are required fields')
