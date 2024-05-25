from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from .choices import ProfileType
from .validations import PasswordNotMatchError, UserAlreadyExistError


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_type", "username", "email", "first_name", "last_name"]


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)
    user_type = serializers.ChoiceField(choices=ProfileType, required=True)

    def validate(self, data):
        if data["password"] != data["repeat_password"]:
            PasswordNotMatchError().raise_error()
        return data

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            UserAlreadyExistError().raise_error()
        return value

    def create(self, validated_data):
        user_data = {
            "username": validated_data["username"],
            "email": validated_data.get("email", ""),
            "first_name": validated_data.get("first_name", ""),
            "last_name": validated_data.get("last_name", ""),
        }
        user = User.objects.create(**user_data)
        profile_data = {"user": user, "user_type": validated_data["user_type"]}
        user.set_password(validated_data["password"])
        profile = Profile.objects.create(**profile_data)
        return profile

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "repeat_password",
            "user_type",
        ]
