from django.contrib import admin

from games.models import ProfileModel, GamesModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GamesModel)
class GamesAdmin(admin.ModelAdmin):
    pass
