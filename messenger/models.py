from django.conf import settings
from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class AlertMessage(models.Model):
	sender = models.ForeignKey(User)
	receiver = models.ForeignKey(User)
	message = models.TextField(default='')
	create_datetime = models.DateTimeField(auto_now_add=True)



