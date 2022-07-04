from django.contrib import admin
from account.models import (
    Address,

    User, 
    Supervizor,
    Languages,
    Skills,
    WorkExperiences,
    UserAddress,

    Customer,
    CustomerAddress,

)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    pass

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass

@admin.register(Supervizor)
class SupervizorAdmin(admin.ModelAdmin):
    pass

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkExperiences)
class WorkExperiencesAdmin(admin.ModelAdmin):
    pass