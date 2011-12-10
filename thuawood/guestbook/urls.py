from django.conf.urls.defaults import patterns, include, url

from . import views
urlpatterns = patterns('',
    url('^$', views.gastbok, name='gastbok'),
    url('^/skriv/$', views.skriv, name='skriv'),
)
