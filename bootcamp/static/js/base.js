function showPassword() {
	document.getElementById('password1').type='text'
	}
function hidePassword() {
	document.getElementById('password1').type='password'
	}

function tog(){
	$(document).ready(function(){
		$(".flip").click(function(){
			$(".panel").toggle();
		    });
		});
}


