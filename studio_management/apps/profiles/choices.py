from django.db import models


class ProfileType(models.TextChoices):

    CUSTOMER = ("customer", "Customer")
    STUDIO_OWNER = ("studio_owner", "Studio Owner")
