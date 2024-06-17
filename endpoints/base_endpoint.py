import allure
import logging

from scr.http_client import HTTPClient
from config import URL


class Endpoint:
    response = None
    http_client = HTTPClient(URL)

    def check_status_code_is_(self, status_code):
        with allure.step(f'Проверяем код ответа. Код ответа - {self.response.status_code}'):
            assert self.response.status_code == status_code

    def check_response_field_success_is_(self, value):
        with allure.step(f"Проверяем значение поля 'success' в ответе ({self.response.json()['success']})"):
            assert self.response.json()['success'] == value

    def check_response_field_message_is_(self, value):
        with allure.step(f"Проверяем значение поля 'message' в ответе ({self.response.json()['message']})"):
            assert self.response.json()['message'] == value
