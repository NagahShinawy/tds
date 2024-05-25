from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer, ProfileSerializer
from .models import Profile
from .permissions import IsAdminOrOwner


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all().order_by("-created")
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def perform_destroy(self, instance):
        if instance.user:
            instance.user.delete()
        super().perform_destroy(instance)
