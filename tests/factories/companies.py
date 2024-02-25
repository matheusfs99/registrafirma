import factory
from faker import Faker
from utils.generate_cnpj import generate_cnpj
from apps.companies.models import Company, Employee
from .accounts import UserFactory

faker = Faker()


class CompanyFactory(factory.django.DjangoModelFactory):
    cnpj = factory.LazyFunction(generate_cnpj)
    name = "test ltda"
    fantasy_name = "test"
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Company


class EmployeeFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    company = factory.SubFactory(CompanyFactory)

    class Meta:
        model = Employee
