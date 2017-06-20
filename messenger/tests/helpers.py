from django.contrib.auth.models import User

from messenger.models import Message, Conversation

def create_user(username):
	user = User.objects.create(username=username)
	user.set_password('12345')
	return user


def create_conversation(users):
	conversation = Conversation.objects.create()
	for user in users:
		conversation.participants.add(user)
	return conversation

def create_message(author, conversation):
	Message.objects.create(author=author, conversation=conversation,
		message="Hello, Friend!")