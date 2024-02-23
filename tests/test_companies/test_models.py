import pytest

pytestmark = pytest.mark.django_db


def test_simple_company(company):
    assert company
    assert isinstance(company.cnpj, str)
