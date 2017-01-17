import os

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.core.management.base import BaseCommand, CommandError
from thuawood.guestbook.models import Entry


class Command(BaseCommand):

    def handle(self, *args, **options):
        from django.db import connections
        cursor = connections['legacy'].cursor()
        cursor.execute('''
        select
        name, email, homepage, city, comment, create_date
        from guestbook_entry order by random() limit 1000''')
        for row in cursor.fetchall():
            name, email, homepage, city, comment, create_date = row
            entry, _ = Entry.objects.get_or_create(
                name=name,
                email=email,
                homepage=homepage,
                city=city,
            )
            entry.comment = comment
            entry.create_date = create_date
            entry.save()
            print(entry)
