 var port = chrome.extension.connect({
      name: "popup and background"
 });
 var summary = true;
  port.postMessage("starting up");
 port.onMessage.addListener(function(msg) {
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
    data = JSON.parse(msg);
    entity_name = data.company_name;
    main_sent = data.main_article_sentiment;
    add_sent = data.other_articles_sentiment;
    add_titles = data.other_articles_titles;

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
        document.getElementById("summary").innerHTML = "This is the article summary";
        document.getElementById("summaryButton").style.backgroundColor = "#ddd"
        document.getElementById("summaryButton").style.color = "#5c5b5b"
    }
    else {
        summary = true;
        document.getElementById("summary").innerHTML = "";
        document.getElementById("summaryButton").style.backgroundColor = "#53739f"
        document.getElementById("summaryButton").style.color = "white"
    }

}