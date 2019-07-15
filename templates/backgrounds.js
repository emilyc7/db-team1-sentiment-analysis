// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
	// Send a message to the active tab
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
		var activeTab = tabs[0];
		chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
	});
});

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "open_new_tab" ) {
      chrome.tabs.create({"url": request.url});
    }
  }
);

// XMLHttpRequest starts here
window.onload = function() {
	//create event listener when the button is clicked
	document.getElementById('sentiment-btn').addEventListener('click', loadSentiment);
	document.getElementById('stock-btn').addEventListener('click', loadStock);
}

// loads the sentiment
function loadSentiment() {
	// Creates XMLHttpRequest object
	var request = new XMLHttpRequest();

	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
	});

	request.open('POST', 'http://192.168.99.100:4000/', true);
	request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	request.onload = function(){
		// check status of response -if 200 it means everything is okay-
		if(this.readyState == 4 && this.status == 200){
			document.body.innerHTML = this.responseText;
		}
	}
	// Sends request
	request.send({"url": url});
}

// loads the stock
function loadStock() {
	// Creates XMLHttpRequest object
	var request = new XMLHttpRequest();

	// OPEN: type of request, url/txt, async
	request.open('GET', 'sample1.json', true);

	request.onload = function(){
		// check status of response -if 200 it means everything is okay-
		if(this.readyState == 4 && this.status == 200){
			document.getElementById('serverResponse').innerHTML = "hello";
		}
	}
	// Sends request
	request.send();
}
