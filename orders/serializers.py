from rest_framework import serializers


class OrderItemCreateSerializer(serializers.Serializer):

    product = serializers.IntegerField()

    quantity = serializers.IntegerField(min_value=1)

class OrderCreateSerializer(serializers.Serializer):
    """
    Represents the complete order request.
    """
    warehouse = serializers.IntegerField()

    shipping_address = serializers.CharField()

    notes = serializers.CharField(
        required=False,
        allow_blank=True
    )

    items = OrderItemCreateSerializer(
        many=True
    )