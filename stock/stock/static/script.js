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

// $( document ).ready(function() {
// 	$( "body iframe" ).appendTo(".tradingview-widget-container");

	// var chart = LightweightCharts.createChart(document.body, {
	// 	width: 600,
	//   height: 300,
	// 	layout: {
	// 		backgroundColor: '#000000',
	// 		textColor: 'rgba(255, 255, 255, 0.9)',
	// 	},
	// 	grid: {
	// 		vertLines: {
	// 			color: 'rgba(197, 203, 206, 0.5)',
	// 		},
	// 		horzLines: {
	// 			color: 'rgba(197, 203, 206, 0.5)',
	// 		},
	// 	},
	// 	crosshair: {
	// 		mode: LightweightCharts.CrosshairMode.Normal,
	// 	},
	// 	priceScale: {
	// 		borderColor: 'rgba(197, 203, 206, 0.8)',
	// 	},
	// 	timeScale: {
	// 		borderColor: 'rgba(197, 203, 206, 0.8)',
	// 	},
	// });
	
	// var candleSeries = chart.addCandlestickSeries({
	//   upColor: 'rgba(255, 144, 0, 1)',
	//   downColor: '#000',
	//   borderDownColor: 'rgba(255, 144, 0, 1)',
	//   borderUpColor: 'rgba(255, 144, 0, 1)',
	//   wickDownColor: 'rgba(255, 144, 0, 1)',
	//   wickUpColor: 'rgba(255, 144, 0, 1)',
	// });
	
	// fetch('https://finnhub.io/api/v1/stock/candle?symbol=IBM&resolution=D&from=1572651390&to=1575243390&token=bs9jpfnrh5rahoaohehg'/*, { 
	// 	body: JSON.stringify({json: true})
	// }*/).then( (res) => res.json()).then(data => {
	// 	console.log(data)
	//   var cd = []
	// 	data.t.forEach((item,i) => {
	// 		 var date = new Date(item*1000)
	// 	var dateString = date.getFullYear()+'-'+(date.getMonth()+1)+'-'+date.getDate();
	// 	  cd.push({time: dateString, high: data.h[i], low: data.l[i], close: data.c[i], open: data.o[i]})
	  
	//   });
	//   console.log(cd);
	//   candleSeries.setData(cd);
	// })
	
// });



