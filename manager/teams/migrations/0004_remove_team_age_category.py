# Generated by Django 4.1.5 on 2023-01-25 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0003_team_age_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="age_category",
        ),
    ]
