from rest_framework import serializers
from .models import Studio


class StudioSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Studio
        fields = '__all__'
