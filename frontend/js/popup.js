 var port = chrome.extension.connect({
      name: "popup and background"
 });
  port.postMessage("starting up");
 port.onMessage.addListener(function(msg) {
    data = JSON.parse(msg);
    document.getElementById("sent-circle").setAttribute("data-progress", "15");
 });