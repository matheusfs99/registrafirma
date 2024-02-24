import pytest
from apps.accounts.models import User
from apps.companies.models import Company
from apps.companies.serializers import EmployeeSerializer

pytestmark = pytest.mark.django_db


def test_employee_serializer(employee):
    serializer = EmployeeSerializer(instance=employee)
    assert serializer.data == {
        "id": employee.id,
        "user": employee.user.id,
        "company": employee.company.id
    }


def test_employee_serializer_without_required_fields():
    incomplete_data = {
        "user": "1"
    }
    serializer = EmployeeSerializer(data=incomplete_data)
    assert not serializer.is_valid()


def test_employee_serializer_create(employee_payload):
    serializer = EmployeeSerializer(data=employee_payload)
    assert serializer.is_valid()
    validated_data = serializer.validated_data
    employee = serializer.create(validated_data)

    assert employee.id
