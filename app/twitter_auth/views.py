import cgi
from oauth2 import Consumer, Client, Token

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from twitter_auth import settings as twitter_auth_settings
from twitter_auth.exceptions import TwitterAuthException

consumer = Consumer(key=settings.TWITTER_CONSUMER_KEY, secret=settings.TWITTER_CONSUMER_SECRET)
client = Client(consumer)

def twitter_login(request):
    response, content = client.request(twitter_auth_settings.REQUEST_TOKEN_URL, "GET")
    if not response.get('status') == '200':
        raise TwitterAuthException('Invalid response from Twitter.', response)
    request.session['oauth_request_token'] = dict(cgi.parse_qsl(content))
    url = "%(authentication_url)s?oauth_token=%(oauth_token)s" % {
        'authentication_url' : twitter_auth_settings.AUTHENTICATE_URL,
        'oauth_token' : request.session['oauth_request_token']['oauth_token'],
    }
    return HttpResponseRedirect(url)

   
@login_required
def twitter_logout(request):
    logout(request)
    url = getattr(settings, 'LOGOUT_URL', twitter_auth_settings.LOGOUT_URL)
    return HttpResponseRedirect(url)

    
def twitter_authenticated(request):
    user = authenticate(
        key=request.session['oauth_request_token']['oauth_token'], 
        secret=request.session['oauth_request_token']['oauth_token_secret']
    )
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            # user is deactivated.
            pass
    else:
        # invalid username and/or password
        pass
    return HttpResponseRedirect('/')
