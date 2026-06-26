from rest_framework import serializers

from .models import Product

from .models import Inventory

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """

    class Meta:
        model = Product

        fields = (
            "id",
            "sku",
            "name",
            "description",
            "price",
            "is_active",
        )

        read_only_fields = (
            "id",
        )

class InventorySerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(
        source="product.name",
        read_only=True,
    )

    warehouse_name = serializers.CharField(
        source="warehouse.name",
        read_only=True,
    )

    class Meta:
        model = Inventory

        fields = (
            "id",
            "product",
            "product_name",
            "warehouse",
            "warehouse_name",
            "physical_stock",
            "reserved_stock",
            "available_stock",
        )