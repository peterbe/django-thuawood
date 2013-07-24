from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('thuawood.busts.urls')),
    url(r'^gastbok', include('thuawood.guestbook.urls')),
    # url(r'^$', 'thuawood.views.home', name='home'),
    # url(r'^thuawood/', include('thuawood.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
