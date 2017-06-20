from django.shortcuts import render
from django.views.generic import View
from django.http import Http404, JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.core import exceptions

import simplejson

from messenger.models import Message, Conversation

class ConversationsView(View):
	def get(self, request):
		status = 200

		user = request.user
		if not user.is_authenticated():
			status = 401
			response_package = {'message': 'User is Not Authenticated'}

	def post(self, request):
		pass

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
		message_dict['author'] = message.author.username
		message_dict['createDate'] = message.create_datetime.isoformat(' ')
		return message_dict

	def get(self, request):
		"""
		Get messages for a given user-receiver pair
		"""
		status = 200
		user = request.user
		if not user.is_authenticated():
			status = 401
			response_package = {'message': 'User is Not authenticated'}
		else:
			conversation_id = request.GET.get('conversationId')
			# TODO: verify convo exists
			conversation = Conversation.objects.get(id=conversation_id)
			# get all messages from conversation
			messages = conversation.messages.all()

			# check if date range...
			start_date = request.GET.get('startDate')
			if start_date:
				# Query is not yet evaluated in django so can chain filters like this
				# without doing additional queries.
				messages = messages.filter(create_date__gte=start_date)
			response_package = {message.id: self._serialize_message(message) for message in messages}
		return JsonResponse(response_package, status=status)

	def post(self, request):
		"""
		create a new message... return response

		"""
		status = 200
		user = request.user
		if not user.is_authenticated():
			status = 401

		response_package = {'okay': 'yes'}
		return JsonResponse(response_package, status=status)

