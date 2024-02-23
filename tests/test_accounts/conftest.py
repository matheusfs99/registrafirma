import pytest


@pytest.fixture
def user_payload():
    return {
        "email": "test@example.com",
        "first_name": "foo",
        "last_name": "bar",
        "password": "testpassword"
    }
