# Generated by Django 4.2.13 on 2024-05-25 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studio",
            old_name="profile",
            new_name="owner",
        ),
    ]
