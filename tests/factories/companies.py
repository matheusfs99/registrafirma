import factory
from apps.companies.models import Company
from .accounts import UserFactory


class CompanyFactory(factory.Factory):
    cnpj = "29276649000111"
    name = "test ltda"
    fantasy_name = "test"
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Company
