from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile
from .choices import ProfileType
from .validations import PasswordNotMatchError, UserNameAlreadyExistError, EmailAlreadyExistError


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ["id", "username", "email", "first_name", "last_name", "user_type"]

    def validate_email(self, value):
        """
        Validate the email field during update.
        """
        user_id = self.instance.user.id if self.instance and self.instance.user else None
        user = User.objects.exclude(pk=user_id).filter(email=value).exists()
        if user:
            EmailAlreadyExistError().raise_error()

        return value

    def validate_username(self, value):
        """
        Validate the username field during update.
        """
        user_id = self.instance.user.id if self.instance and self.instance.user else None
        user = User.objects.exclude(pk=user_id).filter(username=value).exists()

        if user:
            UserNameAlreadyExistError().raise_error()

        return value

    def update(self, instance, validated_data):
        """
        Update and return the instance given the validated data.
        """
        username = validated_data.get('username')
        email = validated_data.get('email', instance.user.email)
        first_name = validated_data.get('first_name', instance.user.first_name)
        last_name = validated_data.get('last_name', instance.user.last_name)
        if username:
            instance.user.username = username

        if email:
            instance.user.email = email

        if first_name:
            instance.user.first_name = first_name

        if last_name:
            instance.user.last_name = last_name

        instance.user.save()

        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.save()
        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    user_type = serializers.ChoiceField(choices=ProfileType, required=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "repeat_password",
            "user_type",
        ]

    def validate(self, data):
        if data["password"] != data["repeat_password"]:
            PasswordNotMatchError().raise_error()
        return data

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            UserNameAlreadyExistError().raise_error()
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            EmailAlreadyExistError().raise_error()
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
        user.save()
        profile = Profile.objects.create(**profile_data)
        return profile
