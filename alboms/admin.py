from django.contrib import admin
from . import models


class MusiceInline(admin.TabularInline):
    model = models.MusicAlbom
    raw_id_fields = ['music']
    

@admin.register(models.Albom)
class AlbomAdmin(admin.ModelAdmin):
    inlines = [MusiceInline]
    list_display = ['title', 'release_date', 'likes']
    
admin.site.register(models.Comment)
admin.site.register(models.CommentReply)