from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^app/', include('app.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^chat/', include('chat.urls')),
    (r'^api/', include('api.urls')),
    url(r'^site-media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }, name='media')
)


urlpatterns += patterns('',
    url(r'^$', 'chat.views.chat_rooms_list', {}, name='list-rooms'),
)
