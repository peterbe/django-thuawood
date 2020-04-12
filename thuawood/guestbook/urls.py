from django.conf.urls import url

from thuawood.guestbook import views

app_name = 'guestbook'

urlpatterns = [
    url('', views.gastbok, name='gastbok'),
    url('^skriv/$', views.skriv, name='skriv'),
]
