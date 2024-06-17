import pytest

from faker import Faker

from endpoints.user_endpoint import UserEndpoints


@pytest.fixture()
def user_endpoints():
    return UserEndpoints()


@pytest.fixture()
def payload_for_create_user():
    fake = Faker()
    payload = {
        "email": fake.email(),
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
    user_endpoints.create_user(payload_for_create_user)
    access_token = user_endpoints.access_token

    yield

    user_endpoints.delete_user()
