from django.db import models


class ProfileType(models.TextChoices):
    """
    Enumeration representing the possible types of profiles in the system.

    Constants:
    - CUSTOMER: Represents a customer profile.
    - STUDIO_OWNER: Represents a studio owner profile.
    """

    CUSTOMER = ("customer", "Customer")
    STUDIO_OWNER = ("studio_owner", "Studio Owner")
