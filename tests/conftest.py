import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories.accounts import UserFactory
from tests.factories.companies import CompanyFactory, EmployeeFactory


register(UserFactory)
register(CompanyFactory)
register(EmployeeFactory)


@pytest.fixture
def api_client(user):
    user.validated = True
    client = APIClient()
    client.force_authenticate(user)
    return client
