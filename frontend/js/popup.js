 var port = chrome.extension.connect({
      name: "popup and background"
 });
 var summary = true;
 port.postMessage("starting up");
 port.onMessage.addListener(function(msg) {
    displayLoadingScreen();
    data = JSON.parse(msg);
    setTimeout(function() {
            displayMainContent();
            displayReady(data);
        }, 30000);
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

function displayLoadingScreen() {
    document.getElementById("container").style.display = "none";
    document.getElementById("summary-container").style.display = "none";
//    document.getElementById("loading-container").style.display = "block";
}

function displayMainContent() {
    document.getElementById("loading-container").style.display = "none";
    document.getElementById("container").style.display = "block";
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
    entity_name = data.company_name;
    main_sent = data.main_article_sentiment;
    add_sent = data.other_articles_sentiment;
    add_titles = data.other_articles_titles;
    add_summary = data.article_summary;
    main_summary = data.main_summary;

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
}
