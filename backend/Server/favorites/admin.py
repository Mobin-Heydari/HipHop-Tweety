from django.contrib import admin
from . import models


class UserMusicFaverInline(admin.TabularInline):
    model = models.UserMusicFaver
    raw_id_fields = ['music']


class UserAlbomeFaverInline(admin.TabularInline):
    model = models.UserAlbomeFaver
    raw_id_fields = ['albome']

@admin.register(models.UserFavorite)
class UserFavoritesAdmin(admin.ModelAdmin):
    inlines = [UserMusicFaverInline, UserAlbomeFaverInline]
    list_display = ['user', 'count']
