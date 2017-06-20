from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View

# super hacky.. don't look!
class LoginView(View):
	LOGIN = 0

	def get(self, request):
		user = User.objects.all()[self.__class__.LOGIN]
		# Using two hardcoded users to skip auth...
		# just login as one or the other
		if self.__class__.LOGIN == 0:
			self.__class__.LOGIN = 1
		else:
			self.__class__.LOGIN = 0

		login(request, user)

		return HttpResponseRedirect(reverse('index'))

class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('index'))	
