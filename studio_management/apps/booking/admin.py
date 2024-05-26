from django.contrib import admin
from .models import Studio, Reservation, Slot


@admin.register(Studio)
class StudioModelAdmin(admin.ModelAdmin):
    """
    Studio model representation
    """

    list_display = (
        "id",
        "name",
        "status",
        "location",
        "opening_day",
        "closing_day",
        "opening_time",
        "closing_time",
        "owner",
        "created",
        "modified",
    )
    list_editable = (
        "name",
        "location",
        "opening_day",
        "closing_day",
        "opening_time",
        "closing_time",
    )
    list_filter = ("owner",)


@admin.register(Reservation)
class ReservationModelAdmin(admin.ModelAdmin):
    """
    Reservation model representation
    """

    list_display = (
        "id",
        "studio",
        "customer",
        "is_canceled",
        "cancellation_at",
        "created",
        "modified",
    )
    list_editable = ("customer",)
    list_filter = ("customer",)


@admin.register(Slot)
class SlotModelAdmin(admin.ModelAdmin):
    """
    Slot model representation
    """

    list_display = (
        "id",
        "starting_day",
        "ending_day",
        "total_days",
        "reservation",
    )
    list_editable = ("starting_day", "ending_day")
