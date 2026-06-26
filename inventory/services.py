from django.db import transaction


def reserve_inventory(inventory, quantity):
    """
    Reserve stock for an order.
    """

    if inventory.available_stock < quantity:
        raise ValueError("Insufficient stock.")

    inventory.reserved_stock += quantity
    inventory.available_stock -= quantity

    inventory.save()


def release_inventory(inventory, quantity):
    """
    Release reserved stock.
    """

    inventory.reserved_stock -= quantity
    inventory.available_stock += quantity

    inventory.save()


def ship_inventory(inventory, quantity):
    """
    Ship reserved stock.
    """

    inventory.physical_stock -= quantity
    inventory.reserved_stock -= quantity

    inventory.save()