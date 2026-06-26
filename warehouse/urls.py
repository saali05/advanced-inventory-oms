from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import WarehouseViewSet

router = DefaultRouter()

router.register(
    r"warehouses",
    WarehouseViewSet,
)

urlpatterns = [
    path("", include(router.urls)),
]