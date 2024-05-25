from django.db import models
from .choices import ProfileType


class ProfileManager(models.Manager):
    """
    Custom manager for the Profile model, providing additional query methods.

    Methods:
    - get_studio_owners(): Returns a queryset of profiles with the 'studio_owner' user type.
    - get_customers(): Returns a queryset of profiles with the 'customer' user type.
    """

    def get_studio_owners(self):
        """
        Returns a queryset of profiles with the 'studio_owner' user type.
        """
        return self.filter(user_type=ProfileType.STUDIO_OWNER)

    def get_customers(self):
        """
        Returns a queryset of profiles with the 'customer' user type.
        """
        return self.filter(user_type=ProfileType.CUSTOMER)
