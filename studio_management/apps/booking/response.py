from django.utils.translation import gettext_lazy as _


class BaseResponse:
    MESSAGE = ""


class ReservationCanceledSuccessfully(BaseResponse):
    MESSAGE = _("reservation_reservation_canceled_successfully")


class ReservationCanNotCanceled(BaseResponse):
    MESSAGE = _("reservation_reservation_cannot_be_canceled_time_passed")


class ReservationNotFound(BaseResponse):
    MESSAGE = _("reservation_reservation_not_found")
