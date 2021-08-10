from django.contrib import admin
from trashcan.models import Can, Occupancy, DoorUsage

# Register your models here.


class CanAdmin(admin.ModelAdmin):
    list_display = (
        'identifier',
        'volume',
        'current_percent',
        'door_counter',
    )
    fields = ('identifier', 'volume', 'current_percent', 'door_counter',)
    readonly_fields = ('current_percent', 'door_counter',)

class DoorUsageAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'time',
        'can',
    )
    fields = ('time', 'can')
    readonly_fields = ('time', 'can')
    list_filter = ('can',)

class OccupancyAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'time',
        'can',
        'percentage',
    )
    fields = ('time', 'can', 'percentage')
    readonly_fields = ('time', 'can', 'percentage')
    list_filter = ('can',)

admin.site.register(Can, CanAdmin)
admin.site.register(Occupancy, OccupancyAdmin)
admin.site.register(DoorUsage, DoorUsageAdmin)