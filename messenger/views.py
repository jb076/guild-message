from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View

from messenger.models import Conversation, Message


class ConversationsView(View):
    def get(self, request):
        status = 200
        response_package = {}

        user = request.user
        target = request.GET.get('target')

        if not user.is_authenticated():
            status = 401
        else:
            target = User.objects.get(username=target)
            # This got ugly.  I would want a better way to filter on participants to ensure its the exact
            # X # of participants.
            conversation = Conversation.objects\
                .filter(participants__in=[user]).filter(participants__in=[target]).first()
            if conversation is None:
                # Would want to a more specific status code here for no convo vs not auth'd
                status = 404
            else:
                conversation = conversation
                response_package = {'conversationId': conversation.id}

        return JsonResponse(response_package, status=status)

    def post(self, request):
        status = 200
        user = request.user
        target_username = request.POST.get('target')

        target = User.objects.get(username=target_username)
        new_conversation = Conversation.objects.create()
        new_conversation.participants.add(user)
        new_conversation.participants.add(target)

        response_package = {'conversationId': new_conversation.id}
        return JsonResponse(response_package, status=status)


class MessagesView(View):
    """
    Endpoint for handling message fetching/creation
    """

    def get(self, request):
        """
        Get messages for a given user-receiver pair
        """
        status = 200
        response_package = []

        user = request.user
        if not user.is_authenticated():
            status = 401
        else:
            conversation_id = request.GET.get('conversationId')
            last_message_id = request.GET.get('lastMessage')

            # Ensure we are getting a request for a conversation
            try:
                conversation = Conversation.objects.get(id=conversation_id, participants__in=[user])
            except Conversation.DoesNotExist:
                status = 404
                conversation = None

            if conversation:
                # get all messages from conversation
                messages = conversation.messages.all()

                # check if we should only be sending since last received
                if last_message_id:
                    last_message = Message.objects.get(id=last_message_id)
                    # Query is not yet evaluated in django so can chain filters like this
                    # without doing additional queries.
                    messages = messages.filter(create_datetime__gt=last_message.create_datetime)

                messages = messages.order_by('create_datetime')
                response_package = [message.serialize() for message in messages]

        return JsonResponse(response_package, safe=False, status=status)

    def post(self, request):
        """
        create a new message... return response

        """
        status = 200
        response_package = {}

        user = request.user
        if not user.is_authenticated():
            status = 401
        else:
            conversation_id = request.POST.get('conversationId')
            message_content = request.POST.get('message')
            conversation = Conversation.objects.get(id=conversation_id)
            message = Message.objects.create(
                author=user,
                message=message_content,
                conversation=conversation
            )

        response_package = [message.serialize()]
        return JsonResponse(response_package, safe=False, status=status)
