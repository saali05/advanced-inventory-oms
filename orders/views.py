from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.models import Product
from warehouse.models import Warehouse

from .serializers import OrderCreateSerializer
from .services import create_order

from django.contrib.auth import get_user_model

class OrderCreateAPIView(APIView):

    def post(self, request):

        serializer = OrderCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        warehouse = Warehouse.objects.get(
            id=data["warehouse"]
        )

        items = []

        for item in data["items"]:

            product = Product.objects.get(
                id=item["product"]
            )

            items.append(
                {
                    "product": product,
                    "quantity": item["quantity"],
                }
            )

        order = create_order(
            User = get_user_model(),
            customer = User.objects.first(),
            warehouse=warehouse,
            items=items,
            shipping_address=data["shipping_address"],
            notes=data.get("notes", ""),
        )

        return Response(
            {
                "message": "Order created successfully",
                "order_number": order.order_number,
                "total_amount": order.total_amount,
            },
            status=status.HTTP_201_CREATED,
        )