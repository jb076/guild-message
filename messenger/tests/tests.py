from django.core.urlresolvers import reverse
from django.test import Client, RequestFactory, TestCase

from messenger.tests import helpers
from messenger.views import MessagesView


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
        self.assertTrue(response.status_code == 200)

    def test_unauthenticated_user(self):
        response = self.client.get(reverse('messages'), {'conversationId': self.conversation.id})
        self.assertTrue(response.status_code == 401)
