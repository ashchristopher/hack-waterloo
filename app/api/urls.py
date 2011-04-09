from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('api.views',
    url(r'^context/$', 'message_context', {}, name='api-message-context'),
) 
