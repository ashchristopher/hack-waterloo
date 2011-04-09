from django.db import models
from django.contrib.auth.models import User

from twitter_auth.signals import twitter_user_created

class TwitterAuthMixin(object):
    """
    Gives the User access to the relavent twitter information.
    """
    @property
    def oauth_token(self):
        return self.twitterauth.oauth_token
    
    @property
    def oauth_secret(self):
        return self.twitterauth.oauth_secret
User.__bases__ += (TwitterAuthMixin,)


class TwitterAuth(models.Model):
    user = models.OneToOneField(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.user.username


def create_twitter_auth(user, *args, **kwargs):
    """
    Signal is called to create a twitter auth model instance.
    """
    TwitterAuth.objects.create(user=user,)
twitter_user_created.connect(create_twitter_auth)