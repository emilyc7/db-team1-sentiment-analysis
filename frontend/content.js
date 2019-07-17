window.onload = function() {
  var url = window.location.toString()
  console.log(url)
  chrome.runtime.sendMessage({ message: 'test', url: url });
  console.log("onload " + Date())
}
