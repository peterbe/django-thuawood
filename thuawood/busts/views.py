from django.conf import settings
from django.shortcuts import render, get_object_or_404
from models import Bust


def home(request):
    data = {}
    return render(request, 'busts/home.html', data)


def bust(request, oid):
    bust = get_object_or_404(Bust, oid=oid)
    data = {'bust': bust}
    return render(request, 'busts/bust.html', data)
