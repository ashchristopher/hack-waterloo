import twitter
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

from twitter_auth.signals import twitter_user_created, twitter_user_authenticated

def oauth(f=None):
    """
    Decorator that creates a oauth object for use with Twitter library.
    """
    def wrapper(profile, *args, **kwargs):
        oauth = twitter.oauth.OAuth(
            token=profile.user.oauth_token, 
            token_secret=profile.user.oauth_secret, 
            consumer_key=settings.TWITTER_CONSUMER_KEY, 
            consumer_secret=settings.TWITTER_CONSUMER_SECRET
        )
        return f(profile, oauth, *args, **kwargs)
    return wrapper


class Profile(models.Model):
    """
    Hold profile data for the user.
    """
    user = models.OneToOneField(User)
    screen_name = models.CharField(max_length=128)
    twitter_id = models.PositiveIntegerField()
    profile_image_url = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name='followers', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    @oauth
    def update_profile(self, oauth):
        twitter_api = twitter.api.Twitter(auth=oauth)
        response = twitter_api.account.verify_credentials()
        self.profile_image_url = response[u'profile_image_url']
        self.verified = response[u'verified']
        self.save()
        
    def get_profile_image(self):
        return self.profile_image_url or reverse('site-media', kwargs={'path' : 'static/images/profiles/default.png'})
        

    
    def __unicode__(self):
        return "Profile: %s" % self.screen_name
        
    
# signal processing
def create_profile(user, screen_name, user_id, *args, **kwargs):
    """
    Create a new profile when a user is created.
    """
    Profile.objects.create(user=user, screen_name=screen_name, twitter_id=user_id)
    
def update_twitter_info(user, *args, **kwargs):
    """
    Update a users profile information using information from twitter.
    """
    profile = user.get_profile()
    profile.update_profile()
    
    
twitter_user_created.connect(create_profile)
twitter_user_authenticated.connect(update_twitter_info)