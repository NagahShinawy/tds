from django.urls import path
from .views import (
    RegistrationView,
    ProfileListView,
    ProfileRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path("", ProfileListView.as_view(), name="list-profiles"),
    path(
        "<int:pk>/",
        ProfileRetrieveUpdateDestroyAPIView.as_view(),
        name="details-profile",
    ),
    path("create/", RegistrationView.as_view(), name="create-profile"),
]
