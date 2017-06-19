from django.test import TestCase, Client


# Test gets
# - Basic Get
# - User Auth
# - Date ranges
# - 
# Test Creation

class MessagesViewTest(TestCase):
	def setUp(self):
		self.client = client()

	def testGet(self):
