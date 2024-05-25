from django.utils.translation import gettext_lazy as _
from studio_management.apps.core.validations import BaseError


class PasswordNotMatchError(BaseError):
    MESSAGE = _("profiles_passwords_do_not_match")


class UserAlreadyExistError(BaseError):
    MESSAGE = _("profiles_username_already_exists")
