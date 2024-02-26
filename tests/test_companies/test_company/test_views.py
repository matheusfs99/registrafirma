import json
import pytest
from pytest_factoryboy.fixture import register
from http import HTTPStatus
from rest_framework import status
from rest_framework.reverse import reverse
from apps.companies.models import Company
from utils.generate_cnpj import generate_cnpj
from tests.factories.companies import CompanyFactory

pytestmark = pytest.mark.django_db

register(CompanyFactory, "another_company")
register(CompanyFactory, "another_company2")


def test_list_companies(api_client, another_company, another_company2):
    another_company.cnpj = generate_cnpj()
    another_company.save()
    another_company2.cnpj = generate_cnpj()
    another_company2.save()
    url = reverse("company-list")
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["results"]) == 2


def test_create_company(api_client, company_payload):
    url = reverse("company-list")
    response = api_client.post(url, company_payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Company.objects.filter(cnpj=company_payload["cnpj"]).exists()


@pytest.mark.parametrize(
    "field", ["cnpj", "name"]
)
def test_create_company_without_field(field, api_client, company_payload):
    company_payload.pop(field)
    url = reverse("company-list")
    response = api_client.post(url, company_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_company(api_client, company):
    company.save()
    url = reverse("company-detail", kwargs={"pk": company.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_company_nonexistent(api_client):
    url = reverse("company-detail", kwargs={"pk": 123})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND
