from django.conf.urls.defaults import *


urlpatterns = patterns('chat.views',
    url(r'^(?P<room_name>[\w-]+)/$', 'chat_room', {}, name='chat_room'),
    (r'^$', direct_to_template, {'template': 'chat/base.html'}),
)
