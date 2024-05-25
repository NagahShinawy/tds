from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


class ProfileListViewTestCase(APITestCase):
    def setUp(self):
        self.john = User.objects.create_user(
            username="john", email="user1@example.com", password="password"
        )
        self.smith = User.objects.create_user(
            username="smith", email="user2@example.com", password="password"
        )
        self.customer = Profile.objects.create(user=self.john, user_type="customer")
        self.studio_owner = Profile.objects.create(
            user=self.smith, user_type="studio_owner"
        )

    def test_list_profiles_authenticated(self):
        # Test listing all profiles when authenticated
        self.client.force_authenticate(user=self.john)
        url = reverse("list-profiles")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), Profile.objects.count())
        serialized_data = ProfileSerializer(
            Profile.objects.all().order_by("-created"), many=True
        ).data
        self.assertEqual(response.data["results"], serialized_data)

    def test_list_profiles_unauthenticated(self):
        # Test listing all profiles when unauthenticated
        self.client.force_authenticate(user=None)
        url = reverse("list-profiles")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
