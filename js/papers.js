$( document ).ready(function() {
//	$(".bibtex").click(function() {
//	    var href = $(this).attr('href');
//		$.ajax({
//            url: href
//        }).done(function(data) {
//            $("#bibtex").html(data);
//            console.log($("#bibtex").html())
//        });
//	});
//	var options = { content : $('#bibtex') };
//	$('.bibtex').popup({
//        content : function(){
//
//            return this.ele.getAttribute('title');
//        }
//    });
    $('.bibtex').popup();
});

