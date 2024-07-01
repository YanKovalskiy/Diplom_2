import allure
import logging

logger = logging.getLogger(__name__)


class TestGetUserOrders:

    @allure.title('Получение заказов авторизированного пользователя')
    def test_get_user_orders(self, new_user, order_endpoints, payload_for_create_order):
        logger.info(f'+=test_get_user_orders=+')
        headers = {"Authorization": new_user['access_token']}
        order_endpoints.create_order(headers, payload_for_create_order)
        hash_order = order_endpoints.hash_order
        order_endpoints.get_user_orders(headers)

        order_endpoints.check_status_code_is_(200)
        order_endpoints.check_response_field_success_is_(True)
        order_endpoints.check_order_hash_is_(hash_order)

    @allure.title('Получение заказов пользователя без авторизации')
    def test_get_user_orders_without_authorization(self, order_endpoints):
        logger.info(f'+=test_get_user_orders_without_authorization=+')
        order_endpoints.get_user_orders(None)

        order_endpoints.check_status_code_is_(401)
        order_endpoints.check_response_field_success_is_(False)
        order_endpoints.check_response_field_message_is_('You should be authorised')
