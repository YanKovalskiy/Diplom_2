import requests
import logging
import json
import allure

from enum import Enum

logger = logging.getLogger(__name__)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logging.getLogger('faker').setLevel(logging.CRITICAL)


class HTTPMethods(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class HTTPClient:
    def __init__(self, url):
        self.url = url

    @allure.step('Отправляем запрос')
    def send_request(self, method, endpoint, **kwargs):
        url = f'{self.url}{endpoint}'
        response = requests.request(method=method, url=url,  **kwargs)
        logger.info(f'URL = {url}')
        logger.info(f'METHOD = {method}')
        logger.info(f'PAYLOAD = {json.dumps(kwargs, indent=4)}')
        logger.info(f'STATUS_CODE = {response.status_code}')
        logger.info(f'RESPONSE = {json.dumps(response.json(), indent=4)}')
        logger.info('='*40)
        return response
