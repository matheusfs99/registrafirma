from django.utils import timezone
from celery import shared_task
from celery.utils.log import get_task_logger
from apps.companies.models import Company
from .clients import consult_cnpj

logger = get_task_logger(__name__)


@shared_task
def check_company():
    logger.info("Start check_company")
    today = timezone.now().date()
    thirty_days_ago = today - timezone.timedelta(days=30)

    counter = 0
    companies = Company.objects.filter(updated_at__date=thirty_days_ago)
    if len(companies) > 0:
        for company in companies:
            content, status_code = consult_cnpj(company.cnpj)
            if status_code == 200:
                company.name = content["nome"]
                company.fantasy_name = content["fantasia"]
                company.status = Company.Status.ACTIVE if content["situacao"] == "ATIVA" else Company.Status.INACTIVE
            elif status_code == 404:
                company.status = Company.Status.NONEXISTENT
            company.save()
            counter += 1
    logger.info(f"Finish check_company - {counter} companies updated")
    return True
