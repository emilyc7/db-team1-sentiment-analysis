// Our labels along the x-axis
var date = ['2019-01-02','2019-01-03','2019-01-04','2019-01-07','2019-01-08','2019-01-09','2019-01-10']
// For drawing the lines
var price = [156.64,147.06,146.73,149.43,149.43,152.06,152.55];
var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: date,
    datasets: [
      { 
        data: price,
		label: "Price(USD)",
		borderColor: "#008000",
		backgroundColor: "#F0FFF0",
		fill: true
      }
    ]
  }
});