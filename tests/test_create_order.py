import allure
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

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self, order_endpoints, payload_for_create_order):
        logger.info(f'+=test_create_order_without_authorization=+')
        order_endpoints.create_order(None, payload_for_create_order)
        order_endpoints.check_status_code_is_(200)
        order_endpoints.check_response_field_success_is_(True)

    @allure.title('Создание заказа без ингредиентов авторизованным пользователем')
    def test_create_order_without_ingredients(self, new_user, user_endpoints, order_endpoints):
        logger.info(f'+=test_create_order_without_ingredients=+')
        headers = {"Authorization": user_endpoints.access_token}
        order_endpoints.create_order(headers, None)
        order_endpoints.check_status_code_is_(400)
        order_endpoints.check_response_field_success_is_(False)
        order_endpoints.check_response_field_message_is_('Ingredient ids must be provided')

    @allure.title('Создание заказа с некорректными хеш ингредиентов авторизованным пользователем')
    def test_create_order_with_incorrect_hash_ingredients(self, new_user, user_endpoints, order_endpoints):
        logger.info(f'+=test_create_order_with_incorrect_hash_ingredients=+')
        headers = {"Authorization": user_endpoints.access_token}
        payload = {
            "ingredients": ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
        }
        order_endpoints.create_order(headers, payload)
        order_endpoints.check_status_code_is_(400)
        order_endpoints.check_response_field_success_is_(False)
        order_endpoints.check_response_field_message_is_('One or more ids provided are incorrect')