from django.conf.urls import patterns, include, url
from feeds import BustFeed

import views
urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url('^snideri$', views.snideri, name='snideri'),
    url('^kontakt$', views.kontakt, name='kontakt'),
    url('^lankar$', views.lankar, name='lankar'),
    url('^bilder/rss.xml', BustFeed()),
    url('^bilder/(.*)', views.bust, name='bust'),
)
