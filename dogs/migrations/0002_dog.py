# Generated by Django 5.0.13 on 2025-03-22 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dog",
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
                ("name", models.CharField(max_length=250, verbose_name="dog name")),
                ("photo", models.ImageField(blank=True, null=True, upload_to="dogs/")),
                ("birth_date", models.DateTimeField(blank=True, null=True)),
                (
                    "breed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dogs.breed"
                    ),
                ),
            ],
            options={
                "verbose_name": "dog",
                "verbose_name_plural": "dogs",
            },
        ),
    ]
