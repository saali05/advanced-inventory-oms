from decimal import Decimal

from django.db import transaction

from inventory.models import Inventory

from .utils import generate_order_number
from inventory.services import reserve_inventory
from .exceptions import InsufficientStockError

from .models import (
    Order,
    OrderItem,
    OrderStatus,
    PaymentStatus,
)
import logging

logger = logging.getLogger(__name__)


def create_order(
    customer,
    warehouse,
    items,
    shipping_address,
    notes=""
    ):
    """
    Create a new customer order.

    This function is responsible for:
    - Validating inventory
    - Reserving stock
    - Creating the order
    - Creating order items
    - Calculating totals
    """

    with transaction.atomic():
        total_amount = Decimal("0.00")

        order = Order.objects.create(
            order_number=generate_order_number(),
            customer=customer,
            status=OrderStatus.PENDING,
            payment_status=PaymentStatus.UNPAID,
            shipping_address=shipping_address,
            total_amount=Decimal("0.00"),
            notes=notes,
        )

        for item in items:
            product = item["product"]
            quantity = item["quantity"]

            inventory = Inventory.objects.select_for_update().get(
                product=product,
                warehouse=warehouse,
            )

            if inventory.available_stock < quantity:
                raise InsufficientStockError(
                    f"{product.name} has insufficient stock."
                )
            reserve_inventory(inventory, quantity)

            unit_price = product.price

            subtotal = unit_price * quantity
            unit_price=unit_price

            OrderItem.objects.create(
                order=order, 
                product=product, 
                quantity=quantity, 
                unit_price=product.price,
                discount=Decimal("0.00"),
                tax=Decimal("0.00"),
                subtotal=subtotal,
                )

            total_amount += subtotal

        order.total_amount = total_amount
        order.save()

        logger.info(
            "rder %s created successfully with total %.2f",
            order.order_number,
            order.total_amount,
    )
    
        return order