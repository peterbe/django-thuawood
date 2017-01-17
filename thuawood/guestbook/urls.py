from django.conf.urls import url

from thuawood.guestbook import views


urlpatterns = [
    url('', views.gastbok, name='gastbok'),
    url('^skriv/$', views.skriv, name='skriv'),
]
