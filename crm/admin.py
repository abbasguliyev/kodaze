from django.contrib import admin
from .models import (
    Contract,
    ContractStage,
    FollowingUser,
    PaymentTerms,
    Quotation,
    Stage,
    Taxes
)
# Register your models here.
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(ContractStage)
class ContractStageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(FollowingUser)
class FollowingUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(PaymentTerms)
class PaymentTermsAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(Taxes)
class TaxesAdmin(admin.ModelAdmin):
    pass