from django.conf.urls.defaults import patterns, include, url

from . import views
urlpatterns = patterns('',
    url('^$', views.home, name='home'),
    url('^bilder/([\w_\-]+)/$', views.bust, name='bust'),
)
