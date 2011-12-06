from django.contrib import admin
from models import Bust

class BustAdmin(admin.ModelAdmin):
    list_display = ('oid', 'title', 'create_date')


admin.site.register(Bust, BustAdmin)
