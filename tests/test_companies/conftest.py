import pytest


@pytest.fixture
def company_payload(user):
    return {
        "cnpj": "29276649000111",
        "name": "test",
        "fantasy_name": "test tlda",
        "user": user.id
    }


@pytest.fixture
def employee_payload(user, company):
    return {
        "user": user.id,
        "company": company.id
    }
