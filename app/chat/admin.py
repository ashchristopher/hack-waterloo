from django.contrib import admin

from chat.models import ChatRoom


class ChatRoomAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(ChatRoom, ChatRoomAdmin)