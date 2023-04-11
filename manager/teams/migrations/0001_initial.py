# Generated by Django 4.1.5 on 2023-01-24 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
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
                        help_text="Club name", max_length=254, verbose_name="Club name"
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("badge_url", models.URLField(blank=True, max_length=1024, null=True)),
                ("badge", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "website_url",
                    models.URLField(blank=True, max_length=1024, null=True),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                        help_text="Team name", max_length=200, verbose_name="Team name"
                    ),
                ),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "deputy",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]