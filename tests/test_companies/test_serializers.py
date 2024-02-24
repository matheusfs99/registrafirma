import pytest
from apps.accounts.models import User
from apps.companies.serializers import CompanySerializer

pytestmark = pytest.mark.django_db


def test_company_serializer(company):
    serializer = CompanySerializer(instance=company)
    assert serializer.data == {
        "id": company.id,
        "cnpj": company.cnpj,
        "name": company.name,
        "fantasy_name": company.fantasy_name,
        "user": company.user.id
    }


def test_company_serializer_without_required_fields():
    incomplete_data = {
        "cnpj": "03792152000162",
        "name": "teste 1tda",
    }
    serializer = CompanySerializer(data=incomplete_data)
    assert not serializer.is_valid()


def test_company_serializer_with_invalid_cnpj():
    invalid_cnpj_data = {
        "cnpj": "123",
        "name": "test ltda",
        "fantasy_name": "test"
    }
    serializer = CompanySerializer(data=invalid_cnpj_data)
    assert not serializer.is_valid()


def test_company_serializer_create(company_payload):
    serializer = CompanySerializer(data=company_payload)
    assert serializer.is_valid()
    validated_data = serializer.validated_data
    user = User.objects.get(id=company_payload["user"])
    validated_data.update({"user": user})
    company = serializer.create(validated_data)

    assert company.id


def test_partial_update_company_serializer(company):
    old_name = company.name
    serializer = CompanySerializer(instance=company, data={"name": "new_name"}, partial=True)
    serializer.is_valid(raise_exception=True)
    updated_company = serializer.save()

    assert updated_company.id == company.id
    assert updated_company.name != old_name
