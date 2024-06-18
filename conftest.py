import pytest
import logging

from faker import Faker

from endpoints.user_endpoint import UserEndpoints

logger = logging.getLogger(__name__)


@pytest.fixture()
def user_endpoints():
    return UserEndpoints()


@pytest.fixture()
def payload_for_create_user():
    fake = Faker()
    payload = {
        "email": f'yva2024{fake.email()}',
        "password": fake.password(),
        "name": fake.user_name()
    }
    return payload


@pytest.fixture()
def payload_for_login(payload_for_create_user):
    payload = {
        "email": payload_for_create_user['email'],
        "password": payload_for_create_user['password']
    }
    return payload


@pytest.fixture()
def new_user(user_endpoints, payload_for_create_user):
    logger.info('+=fixture - new_user=+')
    user_endpoints.create_user(payload_for_create_user)
    access_token = user_endpoints.access_token

    yield

    if access_token is not None:
        headers = {"Authorization": access_token}
        user_endpoints.delete_user(headers)
