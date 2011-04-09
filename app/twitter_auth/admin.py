from django.contrib import admin

from twitter_auth.models import TwitterAuth

class TwitterAuthAdmin(admin.ModelAdmin):
    save_on_top = True
    date_hierarchy = 'date_added'
    
    
admin.site.register(TwitterAuth, TwitterAuthAdmin)
