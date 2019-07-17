// chrome.runtime.onStartup.addEventListener(function() {
// 	console.log("hello");
// };


//
// // XMLHttpRequest starts here
// window.onload = function() {
// 	//create event listener when the button is clicked
// 	//document.getElementById('sentiment-btn').addEventListener('click', loadSentiment());
// 	// document.getElementById('stock-btn').addEventListener('click', loadStock);
// }
chrome.runtime.onMessage.addListener(
  (request, sender, senderResponse) => {
    if(request.message == 'test') {
      
      	var xmlr = new XMLHttpRequest();
        var url = request.url;
        console.log(url)
      	xmlr.open("POST", "http://192.168.99.100:4000/", true);
      	xmlr.setRequestHeader("Content-Type", "application/json");

      	xmlr.onload = function(){
      		// check status of response -if 200 it means everything is okay-
      		if(this.status == 200){
      			console.log(this.responseText);
      		}
      	}
      	// Sends request
      	xmlr.send(JSON.stringify({ "url" : url }));
    }
  }
);
// chrome.browserAction.onClicked.addListener(function(tab) {
//     console.log("opened")
// });
