import allure

from endpoints.base_endpoint import Endpoint


class OrderEndpoints(Endpoint):
    ENDPOINT = '/api/orders'

    @property
    @allure.step('Получаем хеш заказа')
    def hash_order(self):
        return self.response.json()['order']['_id']

    def check_ingredients_in_order(self, ingredients):
        for ingredient_dict in self.response.json()['order']['ingredients']:
            with allure.step(f"Проверяем наличие ингредиента в заказе id={(ingredient_dict['_id'])}, name='{(ingredient_dict['name'])}'"):
                assert ingredient_dict['_id'] in ingredients

    def check_order_hash_is_(self, hash_order):
        assert self.response.json()['orders'][0]['_id'] == hash_order

    @allure.step('Создаем заказ')
    def create_order(self, headers, payload):
        self.response = self.http_client.send_request(self.http_methods.POST, self.ENDPOINT,
                                                      headers=headers, json=payload)

    @allure.title('Получить заказы конкретного пользователя')
    def get_user_orders(self, headers):
        self.response = self.http_client.send_request(self.http_methods.GET, self.ENDPOINT, headers=headers)
