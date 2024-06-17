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

    # @property
    # @allure.step('Получаем e-mail пользователя')
    # def user_email(self):
    #     return self.response.json()['user']['email']
    #
    # @property
    # @allure.step('Получаем пароль пользователя')
    # def user_password(self):
    #     return self.response.json()['user']['password']

    @allure.step('Создаем пользователя')
    def create_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.REG_USER_ENDPOINT, json=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self, header):
        self.response = self.http_client.send_request(HTTPMethods.DELETE, self.USER_ENDPOINT, headers=header)

    @allure.step('Логинимся под пользователем')
    def login_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.LOGIN_USER_ENDPOINT, json=payload)

