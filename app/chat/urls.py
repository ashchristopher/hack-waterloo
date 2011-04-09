from django.conf.urls.defaults import *

urlpatterns = patterns('chat.views',
    url(r'^$', 'chat_rooms_list', {}, name='list-rooms'),
    url(r'^(?P<room_name>[\w-]+)/$', 'chat_room', {}, name='chat_room'),
)
