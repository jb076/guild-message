from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from messenger.views import MessagesView
from messenger.tests import helpers

class ConversationViewTest(TestCase):
	def setUp(self):
		pass

	def test_get(self):
		pass

	def test_post(self):
		pass

	def test_user_verification(self):
		pass

class MessagesViewTest(TestCase):
	@classmethod
	def setUpClass(cls):
		super(MessagesViewTest, cls).setUpClass()
		cls.view = MessagesView

	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.sender = helpers.create_user('jim')
		self.receiver = helpers.create_user('joe')
		self.conversation = helpers.create_conversation([self.sender, self.receiver])
		self.message = helpers.create_message(self.sender, self.conversation)

	def test_get(self):
		request = self.factory.get(reverse('messages'),
				{'conversationId': self.conversation.id})
		request.user = self.sender
		response = self.view.as_view()(request)
		response_content = str(response.content, encoding='utf8')
		self.assertTrue(response.status_code == 200)

	def test_unauthenticated_user(self):
		response = self.client.get(reverse('messages'), {'conversationId': self.conversation.id})
		self.assertTrue(response.status_code == 401)

	def test_get_has_messages(self):
		return True
