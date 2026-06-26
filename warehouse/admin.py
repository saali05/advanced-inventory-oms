from django.contrib import admin

# Register your models here.

from .models import Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "city",
        "is_active",
        "created_at"
    )

    search_fields = (
        "code",
        "name",
        "city"
    )

    list_filter = (
        "is_active",
        "city"
    )