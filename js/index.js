function showEmail() {
	$("#vemail").html("varshney" + String.fromCharCode(64) + "cs" + String.fromCharCode(46) + "umd" + String.fromCharCode(46) + "edu" );
}

function showPhone() {
	$("#vphone").html("(301) 405-6722" );
}

$( document ).ready(function() {
	$("#vemail").on({ 'touchstart' : function() {
		showEmail();
	} });
	$("#vemail").click(function() {
		showEmail();
	});
	$("#vphone").on({ 'touchstart' : function() {
		showPhone();
	} });
	$("#vphone").click(function() {
		showPhone();
	});
});

