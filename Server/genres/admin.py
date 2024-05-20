from django.contrib import admin
from . import models



@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}