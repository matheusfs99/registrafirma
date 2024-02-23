import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories.accounts import UserFactory


register(UserFactory)


@pytest.fixture
def api_client(user):
    user.validated = True
    client = APIClient()
    client.force_authenticate(user)
    return client
