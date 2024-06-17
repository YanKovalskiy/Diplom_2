import allure
import logging

from scr.http_client import HTTPClient
from config import URL

logger = logging.getLogger(__name__)


class Endpoint:
    response = None
    http_client = HTTPClient(URL)

    def check_status_code_is_(self, status_code):
        with allure.step(f'Проверяем код ответа. Код ответа - {self.response.status_code}'):
            logger.info(f'Код ответа - {self.response.status_code}')
            assert self.response.status_code == status_code

    def check_response_field(self, field, response_text):
        with allure.step(f'Проверяем значение поля [{field}] в ответе'):
            assert self.response.json()[field] == response_text

    def check_in_response_is_field_(self, field):
        with allure.step(f'Проверяем есть ли в ответе поле - {field}'):
            assert field in self.response.json()
