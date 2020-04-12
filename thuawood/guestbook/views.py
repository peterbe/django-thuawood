from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Entry
from .forms import Form


def gastbok(request):
    data = {
      'entries': Entry.objects.all().order_by('-create_date')
    }
    return render(request, 'guestbook/gastbok.html', data)


def skriv(request):
    data = {}
    if request.method == "POST":
        form = Form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('guestbook:gastbok'))
    else:
        form = Form(initial={'spamcheck': 'Sto'})
    data['form'] = form
    return render(request, 'guestbook/skriv.html', data)
