from django.conf import settings

from thuawood.busts.models import Bust


def busts(request):
    return {
       'random_busts': Bust.objects.all().order_by('?')[:70],
       'PROJECT_TITLE': settings.PROJECT_TITLE,
    }
