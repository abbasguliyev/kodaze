from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

USER = get_user_model()

class PaymentTerms(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ("-pk",)

    def __str__(self) -> str:
        return self.name

class Taxes(models.Model):
    title = models.CharField(max_length=300)
    percentage = models.FloatField(default=0)

    class Meta:
        ordering = ("-pk",)

class Contract(models.Model):
    salesperson = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=True, related_name="contracts")
    customer = models.ForeignKey("account.Customer", on_delete=models.CASCADE, related_name="contracts")
    title = models.CharField(max_length=350, null=True, blank=True)
    expected_value = models.FloatField(default=0.0)
    priority = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ], 
        default=0
    )

    class Meta:
        ordering = ("-pk",)

class Stage(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("-pk",)

    def __str__(self) -> str:
        return self.name

class ContractStage(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="stages")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name="contracts")

    class Meta:
        ordering = ("-pk",)

class Quotation(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="quotations")
    payment_type = models.ForeignKey(PaymentTerms, on_delete=models.SET_NULL, null=True, blank=True, related_name="quotations")
    expiration = models.DateField()
    product = models.ManyToManyField("product.Product", related_name="quotations")
    product_description = models.CharField(max_length=300)
    quantity = models.FloatField(default=0)
    note = models.TextField(null=True, blank=True)
    taxes = models.ForeignKey(Taxes, on_delete=models.SET_NULL, null=True, blank=True, related_name="quotations")
    subtotal = models.FloatField(default=0)
    total = models.FloatField(default=0)
    terms_and_conditions = models.TextField(blank=True)

    class Meta:
        ordering = ("-pk",)

class FollowingUser(models.Model):
    user = models.ManyToManyField(USER, related_name="following_quotations")
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, related_name="following_users")
    message = models.TextField(blank=True)

    class Meta:
        ordering = ("-pk",)