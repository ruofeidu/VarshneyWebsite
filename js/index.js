function showEmail() {
	$("#vemail").html("varshney" + String.fromCharCode(64) + "cs" + String.fromCharCode(46) + "umd" + String.fromCharCode(46) + "edu" );
}

function showPhone() {
	$("#vphone").html("(301) 405-6722" );
}

function include() {
  var z, i, elmnt, file, xhttp;
  /*loop through a collection of all HTML elements:*/
  z = document.getElementsByTagName("*");
  for (i = 0; i < z.length; i++) {
    elmnt = z[i];
    /*search for elements with a certain atrribute:*/
    file = elmnt.getAttribute("w3-include-html");
    if (file) {
      /*make an HTTP request using the attribute value as the file name:*/
      xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {elmnt.innerHTML = this.responseText;}
          if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
          /*remove the attribute, and call this function once more:*/
          elmnt.removeAttribute("include");
          includeHTML();
        }
      } 
      xhttp.open("GET", file, true);
      xhttp.send();
      /*exit the function:*/
      return;
    }
  }
}

include();

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

