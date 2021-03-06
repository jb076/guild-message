"""guild_message URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from accounts import views as accounts_views
from guild_message import views as guild_message_views
from messenger import views as messenger_views


urlpatterns = [
    url(r'^$', guild_message_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', messenger_views.MessagesView.as_view(), name='messages'),
    url(r'^conversations/', messenger_views.ConversationsView.as_view(), name='conversations'),
    url(r'^login/', accounts_views.LoginView.as_view(), name='login'),
    url(r'^logout/', accounts_views.LogoutView.as_view(), name='logout'),
]
