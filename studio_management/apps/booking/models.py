from django.db import models
from django.utils import timezone
from django.conf import settings
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


class Reservation(CreatedModelMixin, ModifiedModelMixin, models.Model):

    is_canceled = models.BooleanField(default=False)
    cancellation_at = models.DateTimeField(null=True, blank=True)
    studio = models.ForeignKey(
        Studio, on_delete=models.CASCADE, related_name="reservations"
    )

    customer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="reservations"
    )
    info = models.CharField(
        blank=True, null=True, max_length=100
    )  # field helps in debugging

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.pk}, studio={self.studio.name}, "
            f"customer={self.customer.pk}, is_canceled={self.is_canceled}"
        )

    def cancel(self):
        if (
            not self.is_canceled
            and (timezone.now() - self.created).total_seconds()
            / settings.SECONDS_IN_MINUTES
            <= settings.CANCELLATION_TIME_THRESHOLD
        ):
            self.is_canceled = True
            self.cancellation_at = timezone.now()
            self.save()

    def can_be_canceled(self):
        return (
            not self.is_canceled
            and (timezone.now() - self.created).total_seconds()
            / settings.SECONDS_IN_MINUTES
            <= settings.CANCELLATION_TIME_THRESHOLD
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            status = 1 if self.is_canceled else 0
            self.info = f"{self.customer.id}-{self.studio.id}-{status}-{timezone.now()}"
        super().save(*args, **kwargs)


class Slot(models.Model):
    starting_day = models.DateField()
    ending_day = models.DateField()
    total_days = models.PositiveIntegerField(default=1)
    reservation = models.OneToOneField(
        Reservation, on_delete=models.CASCADE, related_name="slot"
    )

    def calculate_total_days(self):
        if self.starting_day and self.ending_day:
            # Calculate the difference between the starting and ending days
            total_days = (self.ending_day - self.starting_day).days + 1
            return total_days
        return 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_starting_day = self.starting_day
        self._initial_ending_day = self.ending_day

    def save(self, *args, **kwargs):
        if (
            not self.pk
            or self.starting_day != self._initial_starting_day
            or self.ending_day != self._initial_ending_day
        ):
            # Only calculate total days if it's a new instance or if starting/ending days have changed
            self.total_days = self.calculate_total_days()
            # Update initial starting_day and ending_day after calculation
            self._initial_starting_day = self.starting_day
            self._initial_ending_day = self.ending_day
        super().save(*args, **kwargs)
