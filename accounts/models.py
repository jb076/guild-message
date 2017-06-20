from django.db import models
from django.contrib.auth.models import User

# Real user modeling would go here in addition to this simple little friends list.

# Create your models here.
class FriendsList(models.Model):
	user = models.ForeignKey(User, related_name='user_friend_list')
	friends = models.ManyToManyField(User)

	def get_friends_list(self):
		return self.friends.all()