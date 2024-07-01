import allure

from endpoints.base_endpoint import Endpoint


class IngredientEndpoints(Endpoint):
    ENDPOINT = '/api/ingredients'

    @property
    @allure.step('Получаем список доступных ингредиентов')
    def ingredients(self):
        response = self.http_client.send_request(self.http_methods.GET, self.ENDPOINT)
        return response.json()['data']
