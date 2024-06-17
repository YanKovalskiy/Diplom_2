import allure
import pytest


class TestLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_by_existing_users(self, user_endpoints, new_user, payload_for_login):
        user_endpoints.login_user(payload_for_login)
        user_endpoints.check_status_code_is_(200)
        user_endpoints.check_response_field_success_is_(True)

    @allure.title('Логин c неверный паролем или логином')
    @pytest.mark.parametrize(
        'required_field',
        ('email', 'password')
    )
    def test_login_with_incorrect_user_data(self, user_endpoints, new_user, payload_for_login, required_field):
        payload_for_login[required_field] = required_field
        user_endpoints.login_user(payload_for_login)
        user_endpoints.check_status_code_is_(401)
        user_endpoints.check_response_field_success_is_(False)
        user_endpoints.check_response_field_message_is_('email or password are incorrect')
