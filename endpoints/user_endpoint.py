import allure

from endpoints.base_endpoint import Endpoint
from scr.http_client import HTTPMethods


class UserEndpoints(Endpoint):
    USER_ENDPOINT = '/api/auth/user'
    REG_USER_ENDPOINT = '/api/auth/register'
    LOGIN_USER_ENDPOINT = '/api/auth/login'

    @property
    @allure.step('Получаем accessToken пользователя')
    def access_token(self):
        return self.response.json()['accessToken']

    @allure.step('Создаем пользователя')
    def create_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.REG_USER_ENDPOINT, json=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self):
        headers = {"Authorization": self.access_token}
        self.response = self.http_client.send_request(HTTPMethods.DELETE, self.USER_ENDPOINT, headers=headers)

    @allure.step('Логинимся под пользователем')
    def login_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.LOGIN_USER_ENDPOINT, json=payload)
