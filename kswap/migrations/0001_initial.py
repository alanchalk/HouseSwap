# Generated by Django 4.2.5 on 2023-09-17 20:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cities_light", "0011_alter_city_country_alter_city_region_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Kashrut",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Enter a kashrut organisation", max_length=200
                    ),
                ),
            ],
            options={"ordering": ["name"],},
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unique ID for this user",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("telno_mobile", models.CharField(max_length=15, unique=True)),
                ("rabbi", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(default="xxx@xxx", max_length=255, unique=True),
                ),
                (
                    "kashrut",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT, to="kswap.kashrut"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        help_text="Unique ID for this property",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("postcode", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("no_of_rooms", models.PositiveIntegerField()),
                ("estimated_value", models.FloatField()),
                ("property_type", models.CharField(max_length=100)),
                ("amenities", models.TextField()),
                ("pet_friendly", models.BooleanField()),
                ("accessibility_features", models.TextField()),
                ("proximity_to_public_transport", models.TextField()),
                ("nearby_attractions", models.TextField()),
                ("succah", models.BooleanField()),
                ("passover_kitchen", models.BooleanField()),
                ("max_occupancy", models.PositiveIntegerField()),
                ("smoking_allowed", models.BooleanField()),
                ("pictures_of_property", models.ImageField(upload_to="properties/")),
                ("home_description", models.TextField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="cities_light.city",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="cities_light.country",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="kswap.user"
                    ),
                ),
            ],
        ),
    ]
