import allure
import pytest
import logging

logger = logging.getLogger(__name__)


class TestChangeUserData:

    @allure.title('Изменение данных авторизированного пользователя')
    @pytest.mark.parametrize(
        'new_email, new_name',
        (
                ('', ''),
                ('email202406180942@email.com', ''),
                ('', 'NewUserName'),
                ('email202406180942@email.com', 'NewUserName'),
        )
    )
    def test_change_authorized_user_data(self, new_user, user_endpoints, new_email, new_name):
        logger.info(f'+=test_change_authorized_user_data[{new_email}, {new_name}]=+')
        email = user_endpoints.user_email if new_email == '' else new_email
        name = user_endpoints.user_name if new_name == '' else new_name
        payload = {
            "email": email,
            "name": name
        }
        user_endpoints.update_user_data(payload)
        user_endpoints.check_status_code_is_(200)
        user_endpoints.check_response_field_success_is_(True)
        user_endpoints.check_user_email_is_(email)
        user_endpoints.check_user_name_is_(name)

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize(
        'new_email, new_name',
        (
                ('', ''),
                ('email202406180942@email.com', ''),
                ('', 'NewUserName'),
                ('email202406180942@email.com', 'NewUserName'),
        )
    )
    def test_change_not_authorized_user_data(self, new_user, user_endpoints, new_email, new_name):
        logger.info(f'+=test_change_authorized_user_data[{new_email}, {new_name}]=+')
        email = user_endpoints.user_email if new_email == '' else new_email
        name = user_endpoints.user_name if new_name == '' else new_name
        payload = {
            "email": email,
            "name": name
        }
        user_endpoints.update_user_data_without_authorization(payload)
        user_endpoints.check_status_code_is_(401)
        user_endpoints.check_response_field_success_is_(False)
        user_endpoints.check_response_field_message_is_('You should be authorised')

    @allure.title('Изменение e-mail пользователя на уже существующий в базе')
    def test_change_email_authorized_user_to_existing_email(self, new_user, user_endpoints, email_existing_user):
        logger.info(f'+=test_change_email_authorized_user_to_existing_email=+')
        payload = {
            "email": email_existing_user,
            "name": user_endpoints.user_name
        }
        user_endpoints.update_user_data(payload)
        user_endpoints.check_status_code_is_(403)
        user_endpoints.check_response_field_success_is_(False)
        user_endpoints.check_response_field_message_is_('User with such email already exists')
