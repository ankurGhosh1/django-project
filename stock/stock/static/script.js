var owl = $('.owl-carousel');
owl.owlCarousel({
	loop:true,
	nav:true,
	margin:15,
	responsive:{
		0:{
			items:1
		},
		600:{
			items:3
		},            
		960:{
			items:5
		},
		1200:{
			items:10
		}
	}
});
owl.on('mousewheel', '.owl-stage', function (e) {
	if (e.deltaY>0) {
		owl.trigger('next.owl');
	} else {
		owl.trigger('prev.owl');
	}
	e.preventDefault();
});

$('.owl-nav').hide();
$('.owl-dots').hide(); 

$('.collapse').collapse();

fetch('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=bs9jpfnrh5rahoaohehg')
.then(res => res.json())
.then(data => console.log(data))


// constructs the suggestion engine
var states = new Bloodhound({
	datumTokenizer: Bloodhound.tokenizers.whitespace,
	queryTokenizer: Bloodhound.tokenizers.whitespace,
	// `states` is an array of state names defined in "The Basics"
	local: states
  });
  
  $('#bloodhound .typeahead').typeahead({
	hint: true,
	highlight: true,
	minLength: 1
  },
  {
	name: 'states',
	source: states
  });