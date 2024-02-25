import pytest

pytestmark = pytest.mark.django_db


def test_simple_employee(employee):
    assert employee
