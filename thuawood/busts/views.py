from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from models import Bust, Embed


@cache_page(60 * 60 * 24)
def home(request):
    data = {}
    return render(request, 'busts/home.html', data)



@cache_page(60 * 60 * 24)
def bust(request, oid):
    bust = get_object_or_404(Bust, oid=oid)
    data = {'bust': bust}
    return render(request, 'busts/bust.html', data)


@cache_page(60 * 60 * 24)
def snideri(request):
    data = {}
    return render(request, 'busts/snideri.html', data)


@cache_page(60 * 60 * 24)
def kontakt(request):
    data = {}
    return render(request, 'busts/kontakt.html', data)


@cache_page(60 * 60 * 24)
def lankar(request):
    data = {}
    data['embeds'] = Embed.objects.all().order_by('create_date')
    return render(request, 'busts/lankar.html', data)
