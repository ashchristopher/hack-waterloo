from django.db import models

class ChatRoom(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name
