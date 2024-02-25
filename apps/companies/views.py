from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.response import Response

from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action in ("list",):
            company_id = self.request.query_params.get("company")
            company = Company.objects.filter(pk=company_id, user=self.request.user).first()
            return self.queryset.filter(company=company)
        return self.queryset.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        if "company" not in self.request.query_params:
            return Response({"error": "query param 'company' is required"}, status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)

