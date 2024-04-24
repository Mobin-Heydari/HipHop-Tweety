from django.contrib import admin
from . import models




@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'artist']
    prepopulated_fields = {'slug': ('artist', 'title',)}
