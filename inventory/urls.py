from django.urls import include, path

from .views import ProductListAPIView
from .views import ProductDetailAPIView

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, InventoryViewSet

router = DefaultRouter()

router.register(
    r"products",
    ProductViewSet,
    basename="products",
)

router.register(
    r"inventory",
    InventoryViewSet,
)

urlpatterns = [
        path(
        "products/",
        ProductListAPIView.as_view(),
        name="product-list",
    ),
        path(
        "products/<int:pk>/",
        ProductDetailAPIView.as_view(),
        name="product-detail",
    ),
    path("", include(router.urls)),
]