from django.conf.urls.defaults import patterns, include, url

from . import views
urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url('^bilder/(.*)', views.bust, name='bust'),
)
