from django.conf import settings
from django.shortcuts import render, get_object_or_404
from models import Bust, Embed


def home(request):
    data = {}
    return render(request, 'busts/home.html', data)


def bust(request, oid):
    bust = get_object_or_404(Bust, oid=oid)
    data = {'bust': bust}
    return render(request, 'busts/bust.html', data)


def snideri(request):
    data = {}
    return render(request, 'busts/snideri.html', data)


def kontakt(request):
    data = {}
    return render(request, 'busts/kontakt.html', data)


def lankar(request):
    data = {}
    data['embeds'] = Embed.objects.all().order_by('create_date')
    return render(request, 'busts/lankar.html', data)
