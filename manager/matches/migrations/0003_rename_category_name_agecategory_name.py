# Generated by Django 4.1.5 on 2023-01-24 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0002_agecategory_venue_last_updated"),
    ]

    operations = [
        migrations.RenameField(
            model_name="agecategory",
            old_name="category_name",
            new_name="name",
        ),
    ]
