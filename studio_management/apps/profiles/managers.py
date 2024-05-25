from django.db import models
from .choices import ProfileType


class ProfileManager(models.Manager):
    def get_studio_owners(self):
        return self.filter(user_type=ProfileType.STUDIO_OWNER)

    def get_customers(self):
        return self.filter(user_type=ProfileType.CUSTOMER)
