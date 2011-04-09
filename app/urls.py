from django.conf.urls.defaults import *
<<<<<<< HEAD
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
=======
from django.conf import settings
>>>>>>> aed3f4bfca2be38939ff1b58c4c8a922e7123d17
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^app/', include('app.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^chat/', include('chat.urls')),
    url(r'^site-media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }, name='media')
)


urlpatterns += patterns('',
    url(r'^$', 'chat.views.chat_rooms_list', {}, name='list-rooms'),
)