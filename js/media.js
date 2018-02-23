function replaceURL(val) {
  var exp = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
  return val.replace(exp,"<a href='$1'>$1</a>"); 
}

$( document ).ready(function() {
	$(".links").html(replaceURL($("this").html()));
});
