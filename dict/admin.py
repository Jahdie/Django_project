from django.contrib import admin

# Register your models here.
from .models import *


class DictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note', 'date_created', 'date_deleted', 'date_updated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'note')



class LocationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'production_id', 'workshop_id', 'compartment_id')
    list_filter = ('production_id', 'workshop_id', 'compartment_id')

admin.site.register(Locations, LocationsAdmin)
admin.site.register(Controller_families, DictAdmin)
admin.site.register(Compartments, DictAdmin)
admin.site.register(Productions, DictAdmin)
admin.site.register(Workshops, DictAdmin)
