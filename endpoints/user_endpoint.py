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
        return self.response.json().get('accessToken', None)

    @property
    @allure.step('Получаем email пользователя')
    def user_email(self):
        return self.response.json()['user']['email']

    @property
    @allure.step('Получаем имя пользователя')
    def user_name(self):
        return self.response.json()['user']['name']

    @allure.step('Создаем пользователя')
    def create_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.REG_USER_ENDPOINT, json=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self, headers):
        self.response = self.http_client.send_request(HTTPMethods.DELETE, self.USER_ENDPOINT, headers=headers)

    @allure.step('Логинимся под пользователем')
    def login_user(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.POST, self.LOGIN_USER_ENDPOINT, json=payload)

    @allure.step('Обновляем данные авторизированного пользователя')
    def update_user_data(self, payload):
        headers = {"Authorization": self.access_token}
        self.response = self.http_client.send_request(HTTPMethods.PATCH, self.USER_ENDPOINT,
                                                      headers=headers, json=payload)

    @allure.step('Обновляем данные пользователя без авторизации')
    def update_user_data_without_authorization(self, payload):
        self.response = self.http_client.send_request(HTTPMethods.PATCH, self.USER_ENDPOINT, json=payload)
