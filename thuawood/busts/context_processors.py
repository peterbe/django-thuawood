from busts.models import Bust


def busts(request):
    data = {
       'random_busts': Bust.objects.all().order_by('?')[:70]
    }
    return data
