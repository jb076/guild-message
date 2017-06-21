$(function(){

	var openConversation;
	var selectedFriend;
	var lastMessage;

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
			selectedFriend = $(this)[0].textContent;
			$(".chatMod").removeClass('hide');
			$.ajax({
				url: 'conversations/',
				method: 'GET',
				data: {'target': selectedFriend},
				success: function(data) {
					openConversation = data.conversationId;
					getMessages();
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
						}
					})
				}
			})
		});


		setInterval(update, 2000);
	})

	// From Django Docs. gets CSRF token for posting
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
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
	var csrfToken = getCookie('csrftoken')

	function getMessages() {
		$(".chatBox").empty();
		if (typeof openConversation !== 'undefined') {
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation,
					'csrfmiddlewaretoken': csrfToken
				},
				success: function(data) {
					addMessages(data);
				}
			})
		}
	}

	function submitMessage() {
		var inputBox = $(".chatInput");
		messages = createMessage(inputBox.val());
		inputBox.val('');
	};

	function createMessage(content) {
		if (typeof openConversation !== 'undefined') {
			console.log('hello!');
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation,
					'csrfmiddlewaretoken': csrfToken,
					'message': content
				},
				method: 'POST',
				success: function(data){
					addMessages(data);
				}
			})
		}
	}

	function addMessages(messages) {
		var chatBox = $(".chatBox");
		for (var i=0; i < messages.length; i += 1) {
			message = messages[i];
			chatBox.append(
				"<p>" + message.author +' '+ message.createTime + ": " + message.message + "</p>"
			);
			if (i === messages.length - 1) {
				lastMessage = message.messageId;
			}
		}
		chatBox.scrollTop(chatBox.prop("scrollHeight"));
	}

	function update() {
		console.log(lastMessage);
		if (typeof openConversation !== 'undefined') {
			$.ajax({
				url: 'messages/',
				data: {
					'conversationId': openConversation,
					'csrfmiddlewaretoken': csrfToken,
					'lastMessage': lastMessage
				},
				success: function(data){
					addMessages(data);
				},
				method: 'get',
			})
		}
	}
});
