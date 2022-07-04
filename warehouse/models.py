from django.db import models
from django.db.models import F

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    address = models.ForeignKey('account.Address', on_delete=models.CASCADE)
    company=models.ForeignKey("company.Company", on_delete=models.SET_NULL, related_name="warehouses", null=True, blank=True)
    office=models.ForeignKey("company.Office", on_delete=models.SET_NULL, related_name="warehouses", null=True, blank=True)

    class Meta:
        ordering = ("-pk",)

    def __str__(self) -> str:
        return f"{self.name}"

class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.name

class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey("product.Product", null=False, on_delete=models.CASCADE, related_name="stocks")
    unity_of_measure = models.ForeignKey(UnitOfMeasure, null=False, on_delete=models.CASCADE, related_name="stocks")

    class Meta:
        ordering = ("-pk",)

    def increase_stock(self, quantity: int, commit: bool = True):
        """Return given quantity of product to a stock."""
        self.quantity = F("quantity") + quantity
        if commit:
            self.save(update_fields=["quantity"])

    def decrease_stock(self, quantity: int, commit: bool = True):
        self.quantity = F("quantity") - quantity
        if commit:
            self.save(update_fields=["quantity"])

    def __str__(self) -> str:
        return f"stok -> {self.warehouse} - {self.product.product_name} - {self.quantity}"