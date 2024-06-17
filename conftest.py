import pytest

from scr.http_client import HTTPClient
from config import URL


@pytest.fixture()
def http_client():
    return HTTPClient(URL)
