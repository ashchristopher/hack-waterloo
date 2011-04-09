from django.contrib import admin

from chat.models import ChatRoom


class ChatRoomAdmin(admin.ModelAdmin):
	pass

admin.site.register(ChatRoom, ChatRoomAdmin)