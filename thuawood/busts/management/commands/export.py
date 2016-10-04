import codecs
import shutil
import os
import datetime
from urllib import urlopen
from django.core.files import File
from django.core.management.base import BaseCommand
from thuawood.busts.models import Bust
#import yaml
import json
from slugify import slugify


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        destination = os.path.abspath(os.path.curdir)
        destination = os.path.join(destination, 'data')
        if not os.path.isdir(destination):
            os.mkdir(destination)

        for bust in Bust.objects.all():
            self._export(bust, destination)

    def _export(self, bust, destination):
        # destination = os.path.join(destination, bust.oid)
        image_destination = os.path.join(destination, 'images')
        if not os.path.isdir(image_destination):
            os.mkdir(image_destination)
        oid = slugify(bust.oid)
        fp = os.path.join(image_destination, '%s.%s' % (
            oid,
            os.path.basename(bust.image.path).split('.')[-1].lower()
        ))
        if not os.path.isfile(bust.image.path):
            print bust.image.path, "DOES NOT EXIST"
            print(bust.oid, bust.title)
            return
        shutil.copyfile(bust.image.path, fp)

        busts_destination = os.path.join(destination, 'busts')
        if not os.path.isdir(busts_destination):
            os.mkdir(busts_destination)

        # bust_fp = os.path.join(busts_destination, '%s.yaml' % oid)
        bust_fp = os.path.join(busts_destination, '%s.json' % oid)

        with codecs.open(bust_fp, 'w', 'utf-8') as f:
            print repr(bust.title)
            print repr(bust.description)
            print
            document = {
                'title': bust.title,#.encode('utf-8'),
                'description': bust.description.encode('utf-8'),
                'published': bust.is_published,
                'date': bust.create_date.isoformat(),
                'image': os.path.basename(fp).encode('utf-8'),
            }
            print repr(document)
            #yaml.safe_dump(document, f, default_flow_style=False)
            json.dump(document, f, indent=4)
