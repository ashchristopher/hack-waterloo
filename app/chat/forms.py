from django import forms
from django.template.defaultfilters import slugify

from chat.models import ChatRoom


class ChatRoomForm(forms.Form):
	name = forms.CharField(label='Create new room')

	def save(self):
		slug = slugify(self.cleaned_data.get('name'))
		room, was_created = ChatRoom.objects.get_or_create(slug=slug)
		room.name = self.cleaned_data.get('name')
		room.save()
		return room

