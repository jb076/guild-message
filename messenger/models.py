from django.contrib.auth.models import User
from django.db import models


class Conversation(models.Model):
    participants = models.ManyToManyField(User)


class Message(models.Model):
    author = models.ForeignKey(User)
    conversation = models.ForeignKey(Conversation, related_name="messages", null=True, default=None)
    message = models.TextField(default='')
    create_datetime = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        message_dict = {}
        message_dict['conversation'] = self.conversation.id
        message_dict['message'] = self.message
        message_dict['messageId'] = self.id
        message_dict['author'] = self.author.username
        message_dict['createTime'] = self.create_datetime.strftime('%H:%M:%S')
        return message_dict
