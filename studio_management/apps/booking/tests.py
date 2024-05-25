from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from studio_management.apps.profiles.models import Profile


class StudioManagementTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )
        self.profile = Profile.objects.create(user=self.user, user_type="studio_owner")

    def test_list_studios_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/studios/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_studios_unauthenticated(self):
        response = self.client.get("/studios/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_studio_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "name": "Studio 1",
            "status": True,
            "location": "https://www.example.com/studio-1",
            "opening_day": "mon",
            "closing_day": "fri",
            "opening_time": "08:00:00",
            "closing_time": "18:00:00",
            "owner": self.user.profile.id,
        }
        response = self.client.post("/studios/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_studio_unauthenticated(self):
        data = {
            "name": "Studio 1",
            "status": True,
            "location": "https://www.example.com/studio-1",
            "opening_day": "mon",
            "closing_day": "fri",
            "opening_time": "08:00:00",
            "closing_time": "18:00:00",
            "owner": self.user.profile.id,
        }
        response = self.client.post("/studios/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
