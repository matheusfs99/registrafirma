from pycpfcnpj.cpfcnpj import cnpj as cnpj_validator
from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {"user": {"read_only": True}}

    def validate_cnpj(self, value):
        valid_cnpj = cnpj_validator.validate(value)
        if not valid_cnpj:
            raise serializers.ValidationError({"cnpj": "Invalid CNPJ"})
        return value
