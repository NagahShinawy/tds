from django.utils.translation import gettext_lazy as _
from studio_management.apps.core.validations import BaseError


class PasswordNotMatchError(BaseError):
    """
    Error class representing a validation error when passwords do not match.

    Attributes:
    - MESSAGE: A translatable message indicating that the passwords do not match.
    """

    MESSAGE = _("profiles_passwords_do_not_match")


class UserNameAlreadyExistError(BaseError):
    """
    Error class representing a validation error when a user with the same username already exists.

    Attributes:
    - MESSAGE: A translatable message indicating that the username already exists.
    """

    MESSAGE = _("profiles_username_already_exists")


class EmailAlreadyExistError(BaseError):
    """
    Error class representing a validation error when a user with the same email already exists.

    Attributes:
    - MESSAGE: A translatable message indicating that the email already exists.
    """

    MESSAGE = _("profiles_email_already_exists")
