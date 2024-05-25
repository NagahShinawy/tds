from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudioViewSet


router = DefaultRouter()
router.register(r'studios', StudioViewSet, basename='studio')

urlpatterns = [
    path('', include(router.urls)),
]
