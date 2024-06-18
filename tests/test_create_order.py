import allure
import pytest
import logging

logger = logging.getLogger(__name__)


class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_authorized_user(self, new_user, user_endpoints, order_endpoints, payload_for_create_order):
        logger.info(f'+=test_create_order_authorized_user=+')
        headers = {"Authorization": user_endpoints.access_token}
        order_endpoints.create_order(headers, payload_for_create_order)
        order_endpoints.check_status_code_is_(200)
        order_endpoints.check_response_field_success_is_(True)
        order_endpoints.check_ingredients_in_order(payload_for_create_order['ingredients'])
