from django.contrib import admin
from .models import Club, Team


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
    )

    list_filter = (
        "name",
        "city"
    )

    fields = [
        "name",
        "city",
        ("badge_url", "badge"),
        "website_url"
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "club",
        "name",
        "deputy"
    )

    list_filter = (
        "club",
    )