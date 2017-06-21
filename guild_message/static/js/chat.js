$(function(){

	var openConversation;
	var selectedFriend;
	var lastMessage;
	var updateInterval;

	// Event Bindings on document ready
	$(document).ready(function(){
		$(".submit").on('click', function(e){
			submitMessage();
		});
		$(document).keypress(function(e){
			if(e.which === 13) {
				submitMessage();
			}
		});

		$(".userList li").on("click", function(e){
			clearInterval(updateInterval);
			selectedFriend = $(this)[0].textContent;

			// Once we have a conversation selected, show the chat box.
			$(".chatMod").removeClass('hide');
			// Either get an existing conversation or create one then open it on the page.
			$.ajax({
				url: 'conversations/',
				method: 'GET',
				data: {'target': selectedFriend},
				success: function(data) {
					openConversation = data.conversationId;
					getMessages();
					updateInterval = setInterval(update, 2000);
				},
				error: function() {
					// Error if no convo exists.
					// Create conversation, then populate (which won't have anything...)
					$.ajax({
						url: 'conversations/',
						method: 'POST',
						data: {
							'csrfmiddlewaretoken': csrfToken,
							'target': selectedFriend
						},
						success: function(data) {
							openConversation = data.conversationId;
							getMessages();
							updateInterval = setInterval(update, 2000);
						}
					});
				}
			});
		});
	});

	var csrfToken = getCookie('csrftoken');

	function createMessage(content) {
		if (typeof openConversation !== 'undefined') {
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation,
					'csrfmiddlewaretoken': csrfToken,
					'message': content
				},
				method: 'POST',
				success: function(data){
					renderMessages(data);
				}
			});
		}
	}

	// From Django Docs. gets CSRF token for posting
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

	function getMessages() {
		// Clear out chat box since we are loading all messages again.
		$(".chatBox").empty();
		if (typeof openConversation !== 'undefined') {
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation
				},
				method: 'GET',
				success: function(data) {
					renderMessages(data);
				}
			});
		}
	}

	function renderMessages(messages) {
		var chatBox = $(".chatBox");
		for (var i=0; i < messages.length; i += 1) {
			message = messages[i];
			chatBox.append(
				"<p>" + message.author +' '+ message.createTime + ": " + 
					message.message + "</p>"
			);
			if (i === messages.length - 1) {
				lastMessage = message.messageId;
			}
		}
		// Only jump scroll bar to bottom if there are new messages.  Was otherwise irksome.
		if (messages.length > 0) {
			chatBox.scrollTop(chatBox.prop("scrollHeight"));
		}
	}

	function submitMessage() {
		var inputBox = $(".chatInput");
		messages = createMessage(inputBox.val());
		inputBox.val('');
	}

	function update() {
		if (typeof openConversation !== 'undefined') {
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation,
					'lastMessage': lastMessage
				},
				success: function(data){
					renderMessages(data);
				},
				method: 'get',
			});
		}
	}
});
