import requests
import logging
import json
import allure

from enum import Enum

logger = logging.getLogger(__name__)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)


class HTTPMethods(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class HTTPClient:
    def __init__(self, url):
        self.url = url

    def send_request(self, method, endpoint, **kwargs):
        url = f'{self.url}{endpoint}'
        session = requests.Session()
        with allure.step('Отправляем запрос'):
            response = session.request(method=method, url=url,  **kwargs)
            logger.info(f'URL = {url}')
            logger.info(f'Status code = {response.status_code}')
            logger.info(f'Response = {json.dumps(response.json(), indent=4)}')
        return response
