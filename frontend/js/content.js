window.onload = function() {
  var url = window.location.toString()
  chrome.runtime.sendMessage({ message: 'url', url: url });
}
