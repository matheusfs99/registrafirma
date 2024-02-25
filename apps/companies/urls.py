from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()
router.register("company", CompanyViewSet, basename="company")
router.register("employee", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("", include(router.urls)),
]
