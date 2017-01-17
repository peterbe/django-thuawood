import os

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.core.management.base import BaseCommand, CommandError
from thuawood.busts.models import Bust, Embed


class Command(BaseCommand):

    def handle(self, *args, **options):
        from django.db import connections
        cursor = connections['legacy'].cursor()
        cursor.execute('''
        select
        oid, title, description, is_published, create_date, image
        from busts_bust order by random()''')
        for row in cursor.fetchall():
            oid, title, description, is_published, create_date, image = row
            image_path = os.path.join(
                settings.LEGACY_MEDIA_ROOT,
                image
            )
            image_path = os.path.abspath(image_path)
            if not os.path.isfile(image_path):
                print("NO VALID IMAGE FOR ", (oid, title))
                continue
            if Bust.objects.filter(oid=oid).exists():
                continue
            bust = Bust.objects.create(
                oid=oid,
                title=title,
                description=description,
                is_published=is_published,
                create_date=create_date,
            )
            with open(image_path, 'rb') as f:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(f.read())
                img_temp.flush()
                bust.image.save(
                    os.path.basename(image_path),
                    File(img_temp)
                )
            print(bust)
