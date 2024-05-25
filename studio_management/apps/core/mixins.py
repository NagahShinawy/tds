from django.db import models


class CreatedModelMixin(models.Model):
    """
    created at field mixin
    """

    created = models.DateTimeField(auto_now_add=True, null=True)  # , verbose_name="created datetime"

    class Meta:
        abstract = True


class ModifiedModelMixin(models.Model):
    """
    modified field mixin
    """

    modified = models.DateTimeField(auto_now=True, null=True, verbose_name="last modified datetime")

    class Meta:
        abstract = True
