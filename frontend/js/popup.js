 var port = chrome.extension.connect({
      name: "Sample Communication"
 });
 port.postMessage("Hi BackGround");
 port.onMessage.addListener(function(msg) {
    data = JSON.parse(msg);

//    document.getElementById("testdiv").innerHTML = data.other_articles_sentiment['one'];
    document.getElementById("sent-tab").innerHTML = "Blentiment";
    document.getElementById("main-sent").setAttribute("data-progress", "15");
 });