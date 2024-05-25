from django.urls import path
from .views import RegistrationView


urlpatterns = [
    # path("", name="list-profiles"),
    path("create/", RegistrationView.as_view(), name="create-profile"),
]
