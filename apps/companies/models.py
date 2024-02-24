from django.db import models


class Company(models.Model):
    cnpj = models.CharField("CNPJ", max_length=14, unique=True)
    name = models.CharField("Razão Social", max_length=255)
    fantasy_name = models.CharField("Nome Fantasia", max_length=255)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)


class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
