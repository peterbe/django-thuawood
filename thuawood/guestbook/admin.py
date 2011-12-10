from django.contrib import admin
from models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'homepage', 'create_date')


admin.site.register(Entry, EntryAdmin)
