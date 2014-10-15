from django.conf.urls import patterns, include, url

import views
urlpatterns = patterns('',
    url('^$', views.gastbok, name='gastbok'),
    url('^/skriv/$', views.skriv, name='skriv'),
)
