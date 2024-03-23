"use strict";
$(document).ready(function() {
	var nextSlide = $("#slides img:first-child");
	var nextCaption;
	var nextSlideSource;
	
	// the function for running the slide show	
	var runSlideShow = function() {   
        $("#caption").fadeOut(3000);
        $("#slide").fadeOut(3000,
        	function () {
       	     	if (nextSlide.next().length == 0) {
					nextSlide = $("#slides img:first-child");
				}
				else {
					nextSlide = nextSlide.next();
				}
				nextSlideSource = nextSlide.attr("src");
				nextCaption = nextSlide.attr("alt"); 
				$("#slide").attr("src", nextSlideSource).fadeIn(3000);					
				$("#caption").text(nextCaption).fadeIn(3000);
			}
		)
	}
	
	// start slide show
    var timer1 = setInterval(runSlideShow, 3000);
    
    
	$("#slide").click(function() {
		if (timer1 != null) {
	    	clearInterval(timer1);
	    	timer1 = null;
		}
		else {
			timer1 = setInterval(runSlideShow, 1000);
		}
	});
	
})