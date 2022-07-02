from django.db import models
from django.core.validators import FileExtensionValidator
from main.image_validator import file_size
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_user_model

USER = get_user_model()

# Create your models here.
class Holding(models.Model):
    holding_name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.holding_name


class Company(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    holding = models.ForeignKey(Holding, on_delete=models.CASCADE, null=True, related_name="companies")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.company_name


class Office(models.Model):
    office_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="offices")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.office_name} Office - {self.company.company_name} Company"


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, related_name="departments")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return f"{self.department_name} Department - {self.office.office_name} Office"


class Position(models.Model):
    position_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, related_name="positions")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="positions")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("pk",)

    def __str__(self):
        return f"{self.position_name} Position - {self.department.department_name} Department - {self.company.company_name} Company"