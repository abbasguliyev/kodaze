from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    price = models.FloatField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-pk",)

    def __str__(self) -> str:
        return self.product_name