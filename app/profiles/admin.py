from django.contrib import admin

from profiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    save_on_top = True
    date_hierarchy = 'date_added'

    
admin.site.register(Profile, ProfileAdmin)