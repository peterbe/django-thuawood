import datetime
import os
import random
import datetime
from django.conf import settings
from django.db import models



def upload_to_bust(instance, filename):
    return _upload_to_product(Bust.UPLOAD_PATH, instance, filename)


def _upload_to_product(upload_path, instance, filename):

    now = datetime.datetime.utcnow()
    steps = [instance.oid,
             now.strftime('%d-%b')]
    dirname = '/'.join(steps)
    if len(filename) > 20:
        # too long, risk of abusing size of database field
        pre, post = os.path.splitext(filename)
        pre = "%s-%s" % (pre[:17], random.randint(100, 1000))
        filename = pre + post

    home = os.path.join(upload_path, dirname)
    filename = base_filename = os.path.join(home, filename)
    c = 0
    while os.path.isfile(filename):
        c += 1
        pre, post = os.path.splitext(base_filename)
        pre += '-%s' % c
        filename = pre + post

    return filename


class Bust(models.Model):
    oid = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=600, blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    UPLOAD_PATH = os.path.join(settings.MEDIA_ROOT, 'photos')
    image = models.ImageField(upload_to=upload_to_bust)

    def __str__(self):
        return '{} ({!r})'.format(self.oid, self.title)

    def get_absolute_url(self):
        return 'busts:bust', [self.oid]


class Embed(models.Model):
    html = models.TextField()
    note = models.CharField(max_length=300, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
