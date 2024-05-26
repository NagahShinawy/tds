from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from studio_management.apps.profiles.choices import ProfileType
from .models import Studio, Reservation
from .serializers import StudioSerializer, ReservationSerializer
from .permissions import IsOwnerOrReadOnly, IsStudioOwner
from .response import ReservationCanceledSuccessfully, ReservationCanNotCanceled, ReservationNotFound


class StudioViewSet(viewsets.ModelViewSet):
    serializer_class = StudioSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ["retrieve", "update", "destroy"]:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [IsStudioOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Filter the queryset based on the user's profile.
        """
        user_profile = self.request.user.profile
        if user_profile.user_type == ProfileType.STUDIO_OWNER:
            return Studio.objects.filter(owner=user_profile)
        return Studio.objects.all()


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        profile = user.profile
        if user.is_staff:
            return Reservation.objects.all()
        if profile.user_type == ProfileType.CUSTOMER:
            return Reservation.objects.filter(customer=profile)

        if profile.user_type == ProfileType.STUDIO_OWNER:
            return Reservation.objects.filter(studio__owner=profile)

        return Reservation.objects.none()


class CustomerReservationCancellationView(generics.UpdateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(customer=user.profile)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().filter(pk=kwargs.get('pk')).first()
        if instance:
            if instance.can_be_canceled():
                instance.cancel()
                return Response({"detail": ReservationCanceledSuccessfully.MESSAGE}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": ReservationCanNotCanceled.MESSAGE}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail":ReservationNotFound.MESSAGE}, status=status.HTTP_404_NOT_FOUND)
