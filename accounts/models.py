from django.contrib.auth.models import User
from django.db import models


# Real user modeling would go here in addition to this simple little friends list.

# Create your models here.
class FriendsList(models.Model):
    user = models.ForeignKey(User, related_name='user_friend_list')
    friends = models.ManyToManyField(User)

    def get_friends(self):
        return self.friends.all()
