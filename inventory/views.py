from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from .models import Product, Inventory
from .serializers import ProductSerializer, InventorySerializer

from rest_framework import viewsets



class ProductListAPIView(generics.ListAPIView):
    """
    Return all active products.
    """

    queryset = Product.objects.filter(
        is_active=True
    )

    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    Return a single product.
    """

    queryset = Product.objects.filter(
        is_active=True
    )

    serializer_class = ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    Complete CRUD API for Products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class InventoryViewSet(viewsets.ModelViewSet):

    queryset = Inventory.objects.select_related(
        "product",
        "warehouse",
    )

    serializer_class = InventorySerializer