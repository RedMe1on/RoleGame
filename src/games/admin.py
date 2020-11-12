from django.contrib import admin

from .models import ProfileModel, GamesModel, PostModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(GamesModel)
class GamesAdmin(admin.ModelAdmin):
    pass


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'game')
    list_display_links = ('__str__',)
    list_filter = ('game',)

