from django.shortcuts import render

from accounts.models import FriendsList


def index(request):
    cxt = {}
    user = request.user
    if not user.is_authenticated():
        cxt['is_logged_in'] = False
        friends = []
    else:
        friends_list = FriendsList.objects.get(user=user)
        friends = friends_list.get_friends()

    cxt['friends'] = [friend.username for friend in friends]
    cxt['user'] = user
    return render(request, 'index.html', cxt)
