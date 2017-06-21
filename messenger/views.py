import datetime

from django.shortcuts import render
from django.views.generic import View
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.core import exceptions

from messenger.models import Message, Conversation

class ConversationsView(View):
	def get(self, request):
		status = 200

		user = request.user
		target = request.GET.get('target')
		if not user.is_authenticated():
			status = 401
			response_package = {'status': 'error', 'message': 'User is Not Authenticated'}
		else:
			# Obviously, this breaks when adding 3 participants, the purpose of
			# conversations...
			target = User.objects.get(username=target)
			conversation = Conversation.objects.filter(participants__in=[user, target]).first()
			if conversation == None:
				status = 404
				response_package = {'status': 'error', 'message': 'User is Not Authenticated'}
			else:
				conversation = conversation
				response_package = {'conversationId': conversation.id}

		return JsonResponse(response_package, status=status)

	def post(self, request):
		status = 200
		user = request.user
		target = request.POST.get('target')
		target = User.objects.get(username=target)
		new_conversation = Conversation.objects.create()
		new_conversation.participants.add(user)
		new_conversation.participants.add(target)
		print(new_conversation.participants.all())
		response_package = {'conversationId': new_conversation.id}
		return JsonResponse(response_package, status=status)

	def put(self, request):
		# Normally wouldn't put this here but giving an idea of where
		# the design was going.  This is where users would be able to
		# add people to a conversation
		pass

class MessagesView(View):
	"""
	Endpoint for handling message fetching/creation
	"""
	def _serialize_message(self, message):
		message_dict = {}
		message_dict['conversation'] = message.conversation.id
		message_dict['message'] = message.message
		message_dict['messageId'] = message.id
		message_dict['author'] = message.author.username
		message_dict['createTime'] = message.create_datetime.strftime('%H:%M:%S')
		return message_dict

	def get(self, request):
		"""
		Get messages for a given user-receiver pair
		"""
		status = 200
		response_package = []
		user = request.user
		if not user.is_authenticated():
			status = 401
		else:
			conversation_id = request.GET.get('conversationId')
			last_message_id = request.GET.get('lastMessage')

			# Ensure we are getting a request for a conversation
			try:
				conversation = Conversation.objects.get(id=conversation_id, participants__in=[user])
			except Conversation.DoesNotExist:
				status = 404
				conversation = None

			if conversation:
				# get all messages from conversation
				messages = conversation.messages.all()

				# check if we should only be sending since last received
				if last_message_id:
					last_message = Message.objects.get(id=last_message_id)
					# Query is not yet evaluated in django so can chain filters like this
					# without doing additional queries.
					messages = messages.filter(create_datetime__gt=last_message.create_datetime)

				messages = messages.order_by('create_datetime')
				response_package = [self._serialize_message(message) for message in messages]

		return JsonResponse(response_package, safe=False, status=status)

	def post(self, request):
		"""
		create a new message... return response

		"""
		status = 200
		response_package = {}

		user = request.user
		if not user.is_authenticated():
			status = 401
		else:
			conversation_id = request.POST.get('conversationId')
			message_content = request.POST.get('message')
			conversation = Conversation.objects.get(id=conversation_id)
			message = Message.objects.create(
				author=user,
				message=message_content,
				conversation=conversation
			)

		response_package = [self._serialize_message(message)]
		return JsonResponse(response_package, safe=False, status=status)

