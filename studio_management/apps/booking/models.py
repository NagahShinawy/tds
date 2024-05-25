from django.db import models
from django.utils import timezone
from studio_management.apps.core.mixins import CreatedModelMixin, ModifiedModelMixin
from studio_management.apps.profiles.models import Profile
from .choices import DaysChoices
from .managers import StudioManager


class Studio(CreatedModelMixin, ModifiedModelMixin, models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    location = models.URLField(max_length=500)
    opening_day = models.CharField(max_length=3, choices=DaysChoices.choices)
    closing_day = models.CharField(max_length=3, choices=DaysChoices.choices)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="studios")
    objects = StudioManager()

    def __str__(self):
        return (
            f"{self.__class__.__name__}(name={self.name}, "
            f"opening={self.opening_day}-{self.opening_time}, "
            f"closing={self.closing_day}-{self.closing_time}, owner={self.owner})"
        )

    @property
    def is_open(self):
        current_day = timezone.now().strftime("%a").lower()
        if self.opening_day <= current_day <= self.closing_day:
            return True
        return False

    def save(self, *args, **kwargs):
        current_day = timezone.now().strftime("%a").lower()
        if self.opening_day <= current_day <= self.closing_day:
            self.status = True
        else:
            self.status = False
        super().save(*args, **kwargs)
