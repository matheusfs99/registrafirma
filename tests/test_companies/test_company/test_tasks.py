from unittest import mock

from apps.companies.models import Company
from apps.companies.tasks import check_company
from apps.companies.clients import consult_cnpj


def test_update_companies_within_30_days(mocker):
    mock_company = mocker.Mock()
    mock_company.cnpj = "123456789"
    mock_company.name = "Company A"
    mock_company.fantasy_name = "Company A"
    mock_company.status = Company.Status.ACTIVE
    mock_company.save.return_value = None
    companies = [mock_company]

    mocker.patch("apps.companies.tasks.Company.objects.filter", return_value=companies)

    mocker.patch("apps.companies.tasks.consult_cnpj",
                 return_value=({"nome": "Company A", "fantasia": "Company A", "situacao": "ATIVA"}, 200))

    check_company()

    assert mock_company.name == "Company A"
    assert mock_company.fantasy_name == "Company A"
    assert mock_company.status == Company.Status.ACTIVE
