	  function drawBasic() {

       var data = new google.visualization.DataTable();
       data.addColumn('string', 'Date');
       data.addColumn('number', 'Apple');

       data.addRows([
         ['2019-01-02', 156.64], ['2019-01-03', 147.06], ['2019-01-04', 146.73], ['2019-01-07', 149.53], ['2019-01-08', 149.53], ['2019-01-09', 152.06], ['2019-01-10', 152.55]
       ]);

       var options = {
		 title: 'Apple INC',
		 legend: 'none',
         hAxis: {
           title: 'Date',
//		   gridlines: {
//				color: 'gray'
//		   }
         },
         vAxis: {
           title: 'Price',
		   gridlines: {
				color: 'transparent'
		   }
         },
		 colors: ['green'],
		 explorer: {
			actions: ['dragToZoom', 'rightClickToReset'],		 
			axis: 'vertical',
			keepInBounds: true,
			maxZoomIn: 4.0
		 }
       };

       var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));

       chart.draw(data, options);
      }