from django.contrib import admin
from .models import Warehouse, Stock, UnitOfMeasure
# Register your models here.
@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    pass