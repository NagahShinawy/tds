from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    """
    Profile model representation
    """

    list_display = ("id", "user", "user_type", "created", "modified")
    list_editable = ("user_type",)
    list_filter = ("user_type",)
