from django.contrib import admin
from . import models




@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'artist']
    prepopulated_fields = {'slug': ('artist', 'title',)}
    

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
