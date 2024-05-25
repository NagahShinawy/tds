from django.contrib import admin
from .models import Studio


@admin.register(Studio)
class StudioModelAdmin(admin.ModelAdmin):
    """
    Studio model representation
    """

    list_display = (
        "id",
        "owner",
        "name",
        "status",
        "location",
        "opening_day",
        "closing_day",
        "opening_time",
        "closing_time",
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
