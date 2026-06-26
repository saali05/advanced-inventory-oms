from django.db import models

# Create your models here.

from warehouse.models import Warehouse

class Product(models.Model):

    sku = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.sku} - {self.name}"
    
class Inventory(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.product.name} - {self.warehouse.name}"
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'warehouse'], 
                name='unique_product_warehouse'
            )
        ]