from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class BaseError:
    MESSAGE = _("base_unknown")

    def raise_error(self):
        raise serializers.ValidationError(self.MESSAGE)
