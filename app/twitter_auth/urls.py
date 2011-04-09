from django.conf.urls.defaults import *

urlpatterns = patterns('twitter_auth.views',
    url(r'^login/?$', 'twitter_login', {}, name='twitter_auth__login'),
    url(r'^login/authenticated/?$', 'twitter_authenticated', {}, name='twitter_auth__authenticated'),
    url(r'^logout/?$', 'twitter_logout', {}, name='twitter_auth__logout'),    
)