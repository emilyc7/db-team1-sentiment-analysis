 var port = chrome.extension.connect({
      name: "Sample Communication"
 });
 port.postMessage("Hi BackGround");
 port.onMessage.addListener(function(msg) {
    data = JSON.parse(msg);

    document.getElementById("sent-circle").setAttribute("data-progress", "15");
 });