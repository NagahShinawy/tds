from django.db import models
from django.utils import timezone


class StudioManager(models.Manager):
    def get_open_studios(self):
        """
        Returns queryset of studios that are currently open.
        """
        current_day = timezone.now().strftime("%a").lower()
        current_time = timezone.now().time()
        return self.filter(
            opening_day__lte=current_day,
            closing_day__gte=current_day,
            opening_time__lte=current_time,
            closing_time__gte=current_time,
        )

    def get_closed_studios(self):
        """
        Returns queryset of studios that are currently closed.
        """
        current_day = timezone.now().strftime("%a").lower()
        current_time = timezone.now().time()
        return self.exclude(
            opening_day__lte=current_day,
            closing_day__gte=current_day,
            opening_time__lte=current_time,
            closing_time__gte=current_time,
        )

