import random
from faker import Faker
from studio_management.apps.profiles.models import Profile
from studio_management.apps.booking.models import Studio
from studio_management.apps.booking.choices import DaysChoices


fake = Faker()


def generate_studios(num_studios):
    studios = []
    for _ in range(num_studios):
        name = fake.company()
        status = random.choice([True, False])
        location = fake.url()
        opening_day = random.choice([choice[0] for choice in DaysChoices.choices])
        closing_day = random.choice([choice[0] for choice in DaysChoices.choices])
        opening_time = fake.time()
        closing_time = fake.time()

        owner = random.choice(Profile.objects.all())

        studio = Studio.objects.create(
            name=name,
            status=status,
            location=location,
            opening_day=opening_day,
            closing_day=closing_day,
            opening_time=opening_time,
            closing_time=closing_time,
            owner=owner,
        )
        studios.append(studio)

    return studios
