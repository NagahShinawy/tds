from django.db import models


class DaysChoices(models.TextChoices):
    """
    Enumeration representing the days of studio in the system.
    """

    MONDAY = ("mon", "Monday")
    TUESDAY = ("tue", "Tuesday")
    WEDNESDAY = ("wed", "Wednesday")
    THURSDAY = ("thu", "Thursday")
    FRIDAY = ("fri", "Friday")
    SATURDAY = ("sat", "Saturday")
    SUNDAY = ("sun", "Sunday")
