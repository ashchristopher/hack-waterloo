from django.conf.urls.defaults import *

urlpatterns = patterns('chat.views',
    url(r'^rooms/$', 'chat_rooms_list', {}, name='list-rooms'),
    url(r'^rooms/(?P<room_name>[\w-]+)/$', 'chat_room', {}, name='chat_room'),
)
