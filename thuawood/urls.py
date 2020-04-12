from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# import thuawood.busts.urls
# import thuawood.guestbook.urls


urlpatterns = [
    url(
        r'',
        include('thuawood.busts.urls', namespace='busts')
    ),
    url(
        r'^gastbok',
        include('thuawood.guestbook.urls', namespace='guestbook')
    ),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
