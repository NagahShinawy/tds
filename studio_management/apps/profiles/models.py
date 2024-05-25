from django.contrib.auth.models import User
from django.db import models
from .choices import ProfileType
from .managers import ProfileManager


class Profile(models.Model):

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
