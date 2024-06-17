import allure

from endpoints.base_endpoint import Endpoint
from scr.http_client import HTTPMethods


class UserEndpoints(Endpoint):

    @allure.step('Создаем пользователя')
    def create_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, '/api/auth/register', json=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self, header):
        self.response = self.http_client.send_request(HTTPMethods.DELETE, '/api/auth/user', headers=header)

    @allure.step('Получаем accessToken пользователя')
    def get_access_token(self):
        return self.response.json()['accessToken']
