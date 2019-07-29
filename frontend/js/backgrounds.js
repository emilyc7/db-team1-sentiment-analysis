var rv;
var rvFlag = 0;
var hasReceived = false;

chrome.runtime.onMessage.addListener(
  (request, sender, senderResponse) => {
    if(request.message == 'url') {

      	var xmlr = new XMLHttpRequest();
        var url = request.url;
        console.log(url)
      	xmlr.open("POST", "http://localhost:5000/sentiment", true);
      	xmlr.setRequestHeader("Content-Type", "application/json");

      	xmlr.onload = function(){
      		// check status of response -if 200 it means everything is okay-
      		if(this.status == 200){
      			console.log(this.responseText);
                rv = this.responseText;
      		}
      	}

      	// Sends request
        rvFlag = 0;
      	xmlr.send(JSON.stringify({ "url" : url }));
    }
  }
);

 chrome.extension.onConnect.addListener(function(port) {
      port.onMessage.addListener(function(msg) { // received connection from popup.js
           if(msg == "starting up")  {
              if(rvFlag == 0) port.postMessage(rvFlag);
              else port.postMessage(rv)
           }
      });
 })
