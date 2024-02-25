import json
import pytest
from pytest_factoryboy.fixture import register
from http import HTTPStatus
from rest_framework import status
from rest_framework.reverse import reverse
from apps.companies.models import Employee
from tests.factories.companies import EmployeeFactory

pytestmark = pytest.mark.django_db

register(EmployeeFactory, "another_employee")
register(EmployeeFactory, "another_employee2")


def test_list_employees(api_client, company, another_employee, another_employee2):
    another_employee.company = company
    another_employee.save()
    another_employee2.company = company
    another_employee2.save()
    url = reverse("employee-list") + f"?company={company.id}"
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["results"]) == 2


def test_list_employees_without_queryparam_company(api_client, company, another_employee, another_employee2):
    another_employee.company = company
    another_employee.save()
    another_employee2.company = company
    another_employee2.save()
    url = reverse("employee-list")
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()["error"] == "query param 'company' is required"


def test_create_employee(api_client, employee_payload):
    queryparam = f"?company={employee_payload['company']}"
    url = reverse("employee-list") + queryparam
    response = api_client.post(url, employee_payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Employee.objects.filter(company=employee_payload["company"]).exists()


@pytest.mark.parametrize(
    "field", ["company", "user"]
)
def test_create_employee_without_field(field, api_client, employee_payload):
    employee_payload.pop(field)
    url = reverse("employee-list")
    response = api_client.post(url, employee_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_employee(api_client, employee):
    employee.save()
    url = reverse("employee-detail", kwargs={"pk": employee.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_employee_nonexistent(api_client):
    url = reverse("employee-detail", kwargs={"pk": 123})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_employee(api_client, employee, another_employee):
    employee.save()
    url = reverse("employee-detail", kwargs={"pk": employee.id})
    payload = {
        "company": another_employee.company.id
    }
    response = api_client.patch(url, json.dumps(payload), content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert employee.id == response.json()["id"]
    assert employee.company != response.json()["company"]
