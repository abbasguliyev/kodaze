from django.contrib import admin
from account.models import (
    Address,
    User, 
    Supervizor,
    UserLanguage,
    Language,
    Skill,
    WorkExperiences,
    Customer,
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

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(UserLanguage)
class UserLanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Supervizor)
class SupervizorAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkExperiences)
class WorkExperiencesAdmin(admin.ModelAdmin):
    pass