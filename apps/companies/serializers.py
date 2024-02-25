from pycpfcnpj.cpfcnpj import cnpj as cnpj_validator
from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", "cnpj", "name", "fantasy_name", "status", "user")
        extra_kwargs = {"user": {"read_only": True}}

    def validate_cnpj(self, value):
        valid_cnpj = cnpj_validator.validate(value)
        if not valid_cnpj:
            raise serializers.ValidationError({"cnpj": "Invalid CNPJ"})
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
