from django.shortcuts import render
from django.views.generic import View

class MessagesView(View):
	"""
	Endpoint for handling message fetching/creation
	"""
	def get(self):
		"""
		Get messages.
		- User/Date range
		
		{status_code: XXX, data: []}
		serialize
		jsonify
		"""
		return False

	def post(self):
		"""
		create a new message... return response

		"""
		return False

