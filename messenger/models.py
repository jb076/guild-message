from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

class Conversation(models.Model):
	participants = models.ManyToManyField(User)

# Create your models here.
class Message(models.Model):
	author = models.ForeignKey(User)
	conversation = models.ForeignKey(Conversation, related_name="messages", null=True, default=None)
	message = models.TextField(default='')
	create_datetime = models.DateTimeField(auto_now_add=True)



