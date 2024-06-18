import allure

from endpoints.base_endpoint import Endpoint


class OrderEndpoints(Endpoint):
    ENDPOINT = '/api/orders'

    @allure.step('Создаем заказ')
    def create_order(self, headers, payload):
        self.response = self.http_client.send_request(self.http_methods.POST, self.ENDPOINT,
                                                      headers=headers, json=payload)

    def check_ingredients_in_order(self, ingredients):
        for ingredient_dict in self.response.json()['order']['ingredients']:
            with allure.step(f"Проверяем наличие ингредиента в заказе id={(ingredient_dict['_id'])}, name='{(ingredient_dict['name'])}'"):
                assert ingredient_dict['_id'] in ingredients
