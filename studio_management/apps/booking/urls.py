from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudioViewSet, ReservationListView, CustomerReservationCancellationView


router = DefaultRouter()
router.register(r"studios", StudioViewSet, basename="studio")

urlpatterns = [
    path("", include(router.urls)),
    path("reservations/", ReservationListView.as_view(), name="list-reservations"),
    path('reservations/<int:pk>/cancel/', CustomerReservationCancellationView.as_view(),
         name='cancel_reservation'),
]
