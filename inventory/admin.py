from django.contrib import admin

# Register your models here.

from .models import Product,Inventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "sku",
        "name",
        "price",
        "is_active",
        "created_at"
    )

    search_fields = (
        "sku",
        "name"
    )

    list_filter = (
        "is_active",
    )

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "warehouse",
        "physical_stock",
        "reserved_stock",
        "available_stock",
    )

    list_filter = (
        "warehouse",
        "product",
    )

    search_fields = (
        "product__name",
        "product__sku",
        "warehouse__name",
    )

    ordering = (
        "warehouse",
        "product",
    )