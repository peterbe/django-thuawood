import datetime
from urllib import urlopen
from django.core.files import File
from django.core.management.base import BaseCommand
from busts.models import Bust


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        content = urlopen('http://www.thuawood.com/export').read()
        content = unicode(content, 'latin1')
        for b in Bust.objects.all():
            b.delete()
        for line in content.splitlines():
            oid, title, description, create_date, photo_title, image_url = line.split('|')
            create_date = datetime.datetime.strptime(create_date, '%Y-%m-%d %H:%M:%S')
            print oid.ljust(20),
            filename = image_url.split('/')[-1]
            tmp_filename = '/tmp/%s_%s' %(oid, filename)
            f = open(tmp_filename, 'wb')
            #with open(tmp_filename, 'wb') as f:
            f.write(urlopen(image_url).read())
            f.close()
            print tmp_filename
            b = Bust.objects.create(
              oid=oid,
              title=title,
              description=description,
              is_published=True,
              create_date=create_date,
              image=File(open(tmp_filename, 'rb'), name=filename),
            )
