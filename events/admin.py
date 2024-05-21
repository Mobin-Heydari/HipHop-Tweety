from django.contrib import admin
from . import models


class EventInline(admin.TabularInline):
    model = models.EventSection
    raw_id_fields = ['event']
    

@admin.register(models.Event)
class AlbomAdmin(admin.ModelAdmin):
    inlines = [EventInline]
    list_display = ['title', 'event_date', 'event_url']
