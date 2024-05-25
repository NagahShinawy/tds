from django.contrib.auth.models import User
from django.db import models
from .choices import ProfileType
from .managers import ProfileManager
from studio_management.apps.core.mixins import ModifiedModelMixin, CreatedModelMixin


class Profile(CreatedModelMixin, ModifiedModelMixin, models.Model):
    """
    Represents a user profile associated with a specific user in the system.

    Attributes:
    - user: One-to-one relationship with the Django User model.
    - user_type: A field representing the type of user, such as 'customer' or 'studio_owner'.
    - objects: Custom manager for the Profile model.

    Note:
    - The Profile model extends the CreatedModelMixin and ModifiedModelMixin to automatically
      track the creation and modification timestamps of profile instances.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=ProfileType.choices)
    objects = ProfileManager()

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name
