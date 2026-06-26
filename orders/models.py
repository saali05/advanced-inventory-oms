from django.db import models

# Create your models here.

from decimal import Decimal

from django.conf import settings

from inventory.models import Product

class OrderStatus(models.TextChoices):

    PENDING = "PENDING", "Pending"

    CONFIRMED = "CONFIRMED", "Confirmed"

    RESERVED = "RESERVED", "Reserved"

    PICKING = "PICKING", "Picking"

    PACKING = "PACKING", "Packing"

    SHIPPED = "SHIPPED", "Shipped"

    DELIVERED = "DELIVERED", "Delivered"

    CANCELLED = "CANCELLED", "Cancelled"

class PaymentStatus(models.TextChoices):

    UNPAID = "UNPAID", "Unpaid"

    PAID = "PAID", "Paid"

    FAILED = "FAILED", "Failed"

    REFUNDED = "REFUNDED", "Refunded"

class Order(models.Model):
    order_number = models.CharField(
    max_length=30,
    unique=True
    )
    
    customer = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
    related_name="orders"
    )

    status = models.CharField(
    max_length=20,
    choices=OrderStatus.choices,
    default=OrderStatus.PENDING
    )
    
    payment_status = models.CharField(
    max_length=20,
    choices=PaymentStatus.choices,
    default=PaymentStatus.UNPAID
    )

    shipping_address = models.TextField(
    blank=True
    )
    
    total_amount = models.DecimalField(
    max_digits=12,
    decimal_places=2,
    default=Decimal("0.00")
    )
    
    notes = models.TextField(
    blank=True
    )
    
    created_at = models.DateTimeField(
    auto_now_add=True
    )
    updated_at = models.DateTimeField(
    auto_now=True
    )

    def __str__(self):
     return self.order_number

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    tax = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    def __str__(self):
        return f"{self.order.order_number} - {self.product.name}"