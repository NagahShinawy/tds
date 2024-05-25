import random
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from faker import Faker
from studio_management.apps.profiles.models import Profile, ProfileType


fake = Faker()
PASS_LEN = 12


def generate_profiles(num_profiles):
    profiles = []
    for _ in range(num_profiles):
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()

        password = fake.password(length=PASS_LEN)
        hashed_password = make_password(password)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
        )

        user_type = random.choice([choice[0] for choice in ProfileType.choices])
        profile = Profile.objects.create(user=user, user_type=user_type)
        profiles.append(profile)

    return profiles
