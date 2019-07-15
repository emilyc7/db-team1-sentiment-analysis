loadSentiment();

// loads the sentiment
function loadSentiment() {
	// Creates XMLHttpRequest object
	var request = new XMLHttpRequest();

	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
    var url = tabs[0].url;
	});

	request.open('POST', 'http://192.168.99.100:4000/', true);
	request.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
	request.onload = function(){
		// check status of response -if 200 it means everything is okay-
		if(this.status == 200){
			console.log(this.responseText);
		}
	}
	// Sends request
	request.send({"url": "google.com"});
};
