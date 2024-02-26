from django.db import models


class Company(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active"
        INACTIVE = "inactive"

    cnpj = models.CharField("CNPJ", max_length=14, unique=True)
    name = models.CharField("Razão Social", max_length=255)
    fantasy_name = models.CharField("Nome Fantasia", max_length=255)
    status = models.CharField("Status", max_length=8, choices=Status.choices, default=Status.ACTIVE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Data de criação", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Data de atualização", auto_now=True)


class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
