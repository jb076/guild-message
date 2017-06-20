$.ajax({
	url: 'messages/',
	data: {'conversationId': 1},
	success: function(data){
		console.log(data);
	},
	method: 'get',
})