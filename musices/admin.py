from django.contrib import admin
from . import models




@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'artist']
    prepopulated_fields = {'slug': ('artist', 'title',)}
    


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'music', 'text', 'created', 'updated']
    list_editable = ['text']
    
admin.site.register(models.CommentReply)