from django.contrib import admin
from . import models



admin.site.register(models.UserMusicFavorite)

admin.site.register(models.UserAlbumFavorite)