
// carousel.js
// =============================================
// This file contains the logic related to the carousel on the homepage
// Gus Wezerek is the original author, go to him with questions


// GLOBALS
// =============================================
var CONFIG = {
	mainExample: $('.example-main'),
	subExamples: $('.example-sub'),
	exampleCounter: 0,
	carouselLen: $('.example-sub').length,
	carouselTimer: 0,
	carouselInterval: 5000,
	exampleTemplate: _.template($('.atlas-example-template').html())
};

// Add our first image
updateCarousel();

// Start the carousel
startCarousel();

// When everything else is ready, load the example thumbnails
$(window).load(addExampleImg());

// HELPERS
// =============================================

function startCarousel() {
	// Don't start the carousel if the main example mod is hidden
	if ( CONFIG.mainExample.css('display') !== 'block' ) {
		return;
	}
	CONFIG.carouselTimer = setInterval(advanceCarousel, CONFIG.carouselInterval);
}

function advanceCarousel() {
	// End the carousel if the main example mod is hidden
	if ( CONFIG.mainExample.css('display') !== 'block' ) {
		clearInterval(CONFIG.carouselTimer);
	}
	if (CONFIG.exampleCounter === CONFIG.carouselLen - 1) {
		CONFIG.exampleCounter = 0;
	} else {
		CONFIG.exampleCounter += 1;
	}

	updateCarousel();
}

function updateCarousel() {
	// Give the new tease the active class
	setActiveTease();

	// Swap the content of the hovered tease
	setMain();
}

function setActiveTease() {
	CONFIG.subExamples.addClass('example-inactive').removeClass('example-active');
	CONFIG.subExamples.eq(CONFIG.exampleCounter).addClass('example-active');
}

function setMain() {
	var $newTease = CONFIG.subExamples.eq(CONFIG.exampleCounter);
	var toAppendString = CONFIG.exampleTemplate({
      img_src: $newTease.data('img-src'),
      caption: $newTease.find('.example-copy').text(),
      slug: $newTease.data('graph-type'),
      ga_label:$newTease.data('ga-label'),
      url: $newTease.find('.example-link').attr('href')
    });

    CONFIG.mainExample.html(toAppendString);
}

// Restarts the carousel timer so the li you just hovered on doesn't advance 
// a second later because of the setInterval in the bground
function restartTimer() {
	clearInterval(CONFIG.carouselTimer);
	startCarousel();
}

function pauseTimer() {
	clearInterval(CONFIG.carouselTimer);
}

function addExampleImg() {
	_.each(CONFIG.subExamples, function(el){
		var $el = $(el);
		$el.find('.example-img').attr('src', $el.data('img-src'));
	});
}


// HANDLERS
// =============================================

CONFIG.subExamples.on({
	mouseenter: function() {
		var newIndex = CONFIG.subExamples.index($(this));
		CONFIG.exampleCounter = newIndex;

		updateCarousel();
		pauseTimer();
	},
	mouseleave: function() {
		CONFIG.subExamples.addClass('example-inactive').removeClass('example-active');
		CONFIG.subExamples.eq(CONFIG.exampleCounter).addClass('example-active');

		restartTimer();
	},

});


// WINDOW RESIZE
// =============================================

// Debounce so that we're not constantly checking for window resizing
var lazyLayout = _.debounce(function() {
	if ( CONFIG.mainExample.css('display') === 'block' ) {
		restartTimer();
	}
}, 100);

$(window).resize(lazyLayout);