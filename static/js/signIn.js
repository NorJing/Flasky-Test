$(function(){
	$('#btnSignIn').click(function(){
		
		$.ajax({
			url: '/signIn',
			data: $('form').serialize(),
			type: 'POST',
			success: function(){
				alert("go to welcome")
			}
		});
	});
});
