from django.contrib import admin

from company.models import (
    Holding,
    Company,
    Office,
    Department,
) 

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

