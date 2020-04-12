from django.conf.urls import url


from thuawood.busts import views
from thuawood.busts import feeds

app_name = 'busts'

urlpatterns = [
    url(
        r'^$',
        views.home,
        name='home'
    ),
    url('^snideri$', views.snideri, name='snideri'),
    url('^kontakt$', views.kontakt, name='kontakt'),
    url('^lankar$', views.lankar, name='lankar'),
    url('^bilder/rss.xml', feeds.BustFeed()),
    url('^bilder/(.*)', views.bust, name='bust'),
]
