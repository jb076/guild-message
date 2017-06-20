from django.shortcuts import render

def index(request):
    cxt = {}
    user = request.user
    if not user.is_authenticated():
    	cxt['is_logged_in'] = False

    # friends_list = FriendsList.objects.get(user=user)
    # friends = friends_list.friends.all()

    # cxt['friends'] = [friend.username for friend in friends]
    cxt['user'] = user
    return render(request, 'index.html', cxt)
