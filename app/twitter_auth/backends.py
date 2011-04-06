import cgi
from oauth2 import Consumer, Token, Client

from django.contrib.auth.models import User
from django.conf import settings

from twitter_auth.models import TwitterAuth
from twitter_auth.signals import twitter_user_created, twitter_user_authenticated
from twitter_auth import settings as twitter_auth_settings
from twitter_auth.exceptions import TwitterAuthException


class TwitterAuthBackend(object):
    """
    Backend for Twitter authorization.
    """
    def authenticate(self, key, secret):
        consumer = Consumer(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        token = Token(key, secret)
        client = Client(consumer, token)
        response, content = client.request(twitter_auth_settings.ACCESS_TOKEN_URL, "GET")
        if not response.get('status') == '200':
            raise TwitterAuthException("Invalid response from Twitter.", response)
        access_token = dict(cgi.parse_qsl(content))
        
        # if we have an access token, it means we have authenticated with Twitter
        user, created = User.objects.get_or_create(username=access_token['screen_name'])
        if created:
            twitter_user_created.send(
                sender="TwitterAuth", 
                user=user, 
                screen_name=access_token['screen_name'], 
                user_id=access_token['user_id']
            )
            # give the user a temporary password - it should never be needed since 
            # Twitter is providing the authentication token.
            user.set_password(User.objects.make_random_password(length=12))
            user.save()

        # update credentials
        user.twitterauth.oauth_token = access_token.get('oauth_token')
        user.twitterauth.oauth_secret = access_token.get('oauth_token_secret')
        user.twitterauth.save()
        
        twitter_user_authenticated.send(sender='TwitterAuth', user=user)
        return user
        
    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except:
            return None
    