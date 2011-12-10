from django.conf import settings
from django.contrib.syndication.views import Feed
from busts.models import Bust

class BustFeed(Feed):
    title = settings.PROJECT_TITLE
    link = '/bilder/rss.xml'
    description = "Gubbar, gubbar, gubbar"

    def item_title(self, obj):
        return obj.title

    def item_link(self, obj):
        return obj.get_absolute_url()

    def item_description(self, obj):
        return obj.description

    def items(self):
        return Bust.objects.filter(is_published=True).order_by('-create_date')[:10]
