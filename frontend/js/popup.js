var port = chrome.extension.connect({
  name: "popup and background"
});
var summary = true;
var data;
port.postMessage("starting up");
port.onMessage.addListener(function(msg) {
  if(msg == 0) {
    displayLoadingScreen();
    setTimeout(function() {port.postMessage("starting up")}, 1000);
  }
  else {
    data = JSON.parse(msg);
    displayMainContent();
    displayReady(data);
  }
});

function openTab(evt, eltName) {
  // Declare all variables
  var i, tabcontent, header;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("header");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(eltName).style.display = "block";
  evt.currentTarget.className += " active";
}

function summaryDisplay() {
  if(summary) {
    summary = false;
    document.getElementById("summary").innerHTML = main_summary;
    document.getElementById("summaryButton").style.backgroundColor = "#ddd";
    document.getElementById("summaryButton").style.color = "#5c5b5b";
  }
  else {
    summary = true;
    document.getElementById("summary").innerHTML = "";
    document.getElementById("summaryButton").style.backgroundColor = "#53739f";
    document.getElementById("summaryButton").style.color = "white";
  }

}

function addSummaryDisplay(summ) {
  document.getElementById("container").style.display = 'none';
  document.getElementById("loading-container").style.display = 'none';
  document.getElementById("summary-container").style.display = 'block';
  document.getElementById("addSummary").innerHTML = summ;
}

function linkButtonClick(link) {
    chrome.tabs.create({ url: link });
}

function displayLoadingScreen() {
  document.getElementById("container").style.display = "none";
  document.getElementById("summary-container").style.display = "none";
  //    document.getElementById("loading-container").style.display = "block";
}

function displayMainContent() {
  document.getElementById("loading-container").style.display = "none";
  document.getElementById("container").style.display = "block";
  document.getElementById("summary-container").style.display = "none";
  // display the block
}

function back() {
  document.getElementById("container").style.display = 'block';
  document.getElementById("loading-container").style.display = 'none';
  document.getElementById("summary-container").style.display = 'none';
}

function displayReady(data) {
  document.getElementById("container").style.display = "block";
  document.getElementById("loading-container").style.display = "none";
  document.getElementById("add-sent").style.display = "none";
  document.getElementById("stock-graph").style.display = "none";
  document.getElementById("sentiment-btn").addEventListener('click',
  function(){
    openTab(event, 'main-sent');
  }, false)
  document.getElementById("stock-btn").addEventListener('click',
  function() {
    openTab(event, 'add-sent');
  }, false)
  document.getElementById("article-btn").addEventListener('click',
  function() {
    openTab(event, 'stock-graph');
    displayGraph();
  }, false);
  document.getElementById("summaryButton").addEventListener('click',
  function() {
    summaryDisplay();
  }, false);
  document.getElementById("add1-button").addEventListener('click',
  function() {
    addSummaryDisplay(add_summary.one);
  }, false);
  document.getElementById("add2-button").addEventListener('click',
  function() {
    addSummaryDisplay(add_summary.two);
  }, false);
  document.getElementById("add3-button").addEventListener('click',
  function() {
    addSummaryDisplay(add_summary.three);
  }, false);
  document.getElementById("add4-button").addEventListener('click',
  function() {
    addSummaryDisplay(add_summary.four);
  }, false);
  document.getElementById("add5-button").addEventListener('click',
  function() {
    addSummaryDisplay(add_summary.five);
  }, false);
  document.getElementById("back-btn").addEventListener('click',
  function() {
    back();
  }, false);

  document.getElementById("sent-circle-add0-source").addEventListener('click',
  function() {
    linkButtonClick(add_links.one);
  }, false);
  document.getElementById("sent-circle-add1-source").addEventListener('click',
  function() {
    linkButtonClick(add_links.two);
  }, false);
  document.getElementById("sent-circle-add2-source").addEventListener('click',
  function() {
    linkButtonClick(add_links.three);
  }, false);
  document.getElementById("sent-circle-add3-source").addEventListener('click',
  function() {
    linkButtonClick(add_links.four);
  }, false);
  document.getElementById("sent-circle-add4-source").addEventListener('click',
  function() {
    linkButtonClick(add_links.five);
  }, false);

  entity_name = data.company_name;
  main_sent = data.main_article_sentiment;
  add_sent = data.other_articles_sentiment;
  add_titles = data.other_articles_titles;
  add_summary = data.article_summary;
  add_links = data.other_articles_links;
  main_summary = data.main_summary;
  sources = data.other_articles_sources;
  document.getElementById("entity-name").innerHTML = entity_name;
  document.getElementById("sent-circle-main").setAttribute("data-progress", main_sent);
  document.getElementById("sent-circle-add0").setAttribute("data-progress", add_sent.one);
  document.getElementById("sent-circle-add1").setAttribute("data-progress", add_sent.two);
  document.getElementById("sent-circle-add2").setAttribute("data-progress", add_sent.three);
  document.getElementById("sent-circle-add3").setAttribute("data-progress", add_sent.four);
  document.getElementById("sent-circle-add4").setAttribute("data-progress", add_sent.five);
  document.getElementById("sent-circle-add0-title").innerHTML = add_titles.one;
  document.getElementById("sent-circle-add1-title").innerHTML = add_titles.two;
  document.getElementById("sent-circle-add2-title").innerHTML = add_titles.three;
  document.getElementById("sent-circle-add3-title").innerHTML = add_titles.four;
  document.getElementById("sent-circle-add4-title").innerHTML = add_titles.five;
  document.getElementById("sent-circle-add0-source").setAttribute("href", add_links.one);
  document.getElementById("sent-circle-add1-source").setAttribute("href", add_links.two);
  document.getElementById("sent-circle-add2-source").setAttribute("href", add_links.three);
  document.getElementById("sent-circle-add3-source").setAttribute("href", add_links.four);
  document.getElementById("sent-circle-add4-source").setAttribute("href", add_links.five);

  document.getElementById("sent-circle-add0-source").innerHTML = sources.one;
  document.getElementById("sent-circle-add1-source").innerHTML = sources.two;
  document.getElementById("sent-circle-add2-source").innerHTML = sources.three;
  document.getElementById("sent-circle-add3-source").innerHTML = sources.four;
  document.getElementById("sent-circle-add4-source").innerHTML = sources.five;

}

function displayGraph() {
  // Hard coded data
//  var date = ['2019-01-02','2019-01-03','2019-01-04','2019-01-07','2019-01-08','2019-01-09','2019-01-10']
//  var price = [156.64,147.06,146.73,149.43,149.43,152.06,152.55];
  var dates = data.stock_dates;
  var price = data.stock_data;
  var comp = entity_name;
  var last = price[price.length - 1];
  var before = price[0];
  var x = dates.length;
  var i;
  console.log(x);
  var numbers = new Array();
  for (i = 1; i <= x; i++) {
    numbers.push(i);
  }
  console.log(numbers);
  // Builds Chart
  var ctx = document.getElementById("myChart");
  var options = {
         scales: {
            xAxes: [{
                afterTickToLabelConversion: function(data){


                    var xLabels = data.ticks;
                    console.log(xLabels);

                    xLabels.forEach(function (labels, j) {
 //                       xLabels[j] = '';
                        if (j == 8 || j == 9 || j == 14 || j == 15){
                            console.log(j);
                            xLabels[j] = 'January ';
                        }
                        else if (j == 44 || j == 45 || j == 46 || j == 51) {
                            xLabels[j] = "February";
                        }
                        else if (j == 70 || j == 71 || j == 72 || j == 73) {
                            xLabels[j] = "March";
                        }
                        else if (j == 90 || j == 91 || j == 96 || j == 97) {
                            xLabels[j] = "April";
                        }
                        else if (j == 115 || j == 116 || j == 117 || j ==118) {
                            xLabels[j] = "May";
                        }
                        else if (j == 141 || j == 142 || j == 143 || j == 144) {
                            xLabels[j] = "June";
                        }
                        else {
                            xLabels[j] = '';
                        }
                    });
                },

               gridLines: {
                display: false
               }
            }]
        }
}
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [ {
        data: price,
        label: comp,
        lineTension: 0,
        borderColor: "#008000",
        backgroundColor: "#F0FFF0",
        pointBackgroundColor: "transparent",
        pointBorderColor: "transparent",
        fill: true
      }
    ]
  },
   options: options
});
// To determine color of graph based on EOD Data
if (last < before) {
  myChart.data.datasets[0].borderColor = "#FF0000";
  myChart.data.datasets[0].backgroundColor = "#FFE4E1";
}
myChart.update();

}

