/******************************************************************************
	Transforms the basic Twitter Bootstrap Carousel into Fullscreen Mode
	@author Fabio Mangolini
     http://www.responsivewebmobile.com
******************************************************************************/
jQuery(document).ready(function() {
	$('.carousel').carousel({
    	pause: "false",
    	interval: 4000
	});

	$('.carousel').css({'margin': 0, 'width': '70%', 'height': '70%'});
	$('.carousel .item').css({'position': 'relative', 'width': '70%', 'height': '70%'});
	$('.carousel-inner div.item img').each(function() {
		var imgSrc = $(this).attr('src');
		$(this).parent().css({'background': 'url('+imgSrc+') center center no-repeat', '-webkit-background-size': '70% ', '-moz-background-size': '70%', '-o-background-size': '70%', 'background-size': '70%', '-webkit-background-size': 'cover', '-moz-background-size': 'cover', '-o-background-size': 'cover', 'background-size': 'cover'});
		$(this).remove();
	});

	$(window).on('resize', function() {
		$('.carousel').css({'width': '70%', 'height': '70%'});
	});
}); 