import datetime
from urllib import urlopen
from django.core.management.base import BaseCommand
from guestbook.models import Entry


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        content = urlopen('http://www.thuawood.com/gastbok/export?a=b').read()
        content = unicode(content, 'latin1')
        for b in Entry.objects.all():
            b.delete()
        for line in content.splitlines():

            name, email, homepage, comment, create_date, city = line.split('|')
            create_date = datetime.datetime.strptime(create_date, '%Y-%m-%d %H:%M:%S')
            comment = comment.replace('\\n', '\n')
            print name.ljust(20), email.ljust(20), repr(comment[:30])
            Entry.objects.create(
              name=name,
              email=email,
              homepage=homepage,
              comment=comment,
              create_date=create_date,
              city=city,
            )
