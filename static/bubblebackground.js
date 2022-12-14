
// CONTROLS
var bubbliness = 4; // Recommended between 1 and 10
var motionResistance = 3; // Recommended between 1 and 10


// Create layers
$('<div />', { 'class': 'layer layer1'  }).appendTo('body');
$('<div />', { 'class': 'layer layer2'  }).appendTo('body');
$('<div />', { 'class': 'layer layer3'  }).appendTo('body');
$('<div />', { 'class': 'layer layer4'  }).appendTo('body');

// Create bubbles
var xsBubbles = bubbliness*7.5; 
var smBubbles = bubbliness*5; 
var mdBubbles = bubbliness*3; 
var lgBubbles = bubbliness*2; 

// Fill layer 1
for(var i = 0; i < xsBubbles; i++) {
	var topPos = (Math.random() * 100) + '%';
	var leftPos = (Math.random() * 100) + '%';
	$('<div />', { 'class': 'bubble bubble-xs' }).appendTo('.layer1').css("top", topPos).css("left", leftPos);
}
// Fill layer 2
for(var i = 0; i < smBubbles; i++) {
	var topPos = (Math.random() * 100) + '%';
	var leftPos = (Math.random() * 100) + '%';
	$('<div />', { 'class': 'bubble bubble-sm' }).appendTo('.layer2').css("top", topPos).css("left", leftPos);
}
// Fill layer 3
for(var i = 0; i < mdBubbles; i++) {
	var topPos = (Math.random() * 100) + '%';
	var leftPos = (Math.random() * 100) + '%';
	$('<div />', { 'class': 'bubble bubble-md' }).appendTo('.layer3').css("top", topPos).css("left", leftPos);
}
// Fill layer 4
for(var i = 0; i < lgBubbles; i++) {
	var topPos = (Math.random() * 100) + '%';
	var leftPos = (Math.random() * 100) + '%';
	$('<div />', { 'class': 'bubble bubble-lg' }).appendTo('.layer4').css("top", topPos).css("left", leftPos);
}

motionResistance = motionResistance *= -1; // Reverse direction


// Mouse-parallax function
var windowWidth = $(window).width();
if( windowWidth > 1024 ) {
  
  $(window).mousemove(function(event){

    // Get centre of layer
    var centerX = $(window).width() / 2;
    var centerY = $(window).height() / 2;

    // Get mouse coordinates
    var mouseX = event.clientX;
    var mouseY = event.clientY;

    var layer1X = (mouseX - centerX) / (motionResistance/0.2);
    var layer1Y = (mouseY - centerY) / (motionResistance/0.2);


    var layer2X = (mouseX - centerX) / (motionResistance/0.3);
    var layer2Y = (mouseY - centerY) / (motionResistance/0.3);

    var layer3X = (mouseX - centerX) / (motionResistance/0.5);
    var layer3Y = (mouseY - centerY) / (motionResistance/0.5);

    var layer4X = (mouseX - centerX) / (motionResistance/0.75);
    var layer4Y = (mouseY - centerY) / (motionResistance/0.75);

    $('.layer1').css('left', layer1X).css('top', layer1Y);
    $('.layer2').css('left', layer2X).css('top', layer2Y);
    $('.layer3').css('left', layer3X).css('top', layer3Y);
    $('.layer4').css('left', layer4X).css('top', layer4Y);

  });
  
} // end if


// Pop function
if( windowWidth > 1024 ) { // Desktop
	
	$('.bubble').mouseover( function() {
		if ( $(this).hasClass('bubble-wobble') ) {
			var thisBubble = $(this);
			thisBubble.addClass('bubble-pop');
			setTimeout( function() {
				thisBubble.hide();
			}, 500);
		} else {
			$(this).addClass('bubble-wobble');
		}
	});
	
} else { // iPad and smaller
	
	$('.bubble').click( function() {
		var thisBubble = $(this);
		thisBubble.addClass('bubble-pop');
		setTimeout( function() {
			thisBubble.hide();
		}, 500);
	});
}