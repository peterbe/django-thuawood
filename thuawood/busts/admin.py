from django.contrib import admin
from .models import Bust, Embed


class BustAdmin(admin.ModelAdmin):
    list_display = ('oid', 'title', 'create_date')

class EmbedAdmin(admin.ModelAdmin):
    list_display = ('note', 'create_date')



admin.site.register(Bust, BustAdmin)
admin.site.register(Embed, EmbedAdmin)
