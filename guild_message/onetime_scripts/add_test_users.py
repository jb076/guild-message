import logging
import django
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guild_message.settings')
django.setup()

from django.contrib.auth.models import User

from accounts.models import FriendsList

new_user_one, created = User.objects.get_or_create(username='jim', defaults={
	'email': 'jsb@gmail.com',
	'password': 'secretpass'}
)
new_user_two, created = User.objects.get_or_create(username='joe', defaults={
	'email': 'joe@gmail.com',
	'password': 'secretpass'}
)

friend_list_one, created = FriendsList.objects.get_or_create(user=new_user_one)
friend_list_one.friends.add(new_user_two)

friend_list_two, created = FriendsList.objects.get_or_create(user=new_user_two)
friend_list_two.friends.add(new_user_one)

