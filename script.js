chrome.storage.sync.get('text',function(res){
	document.getElementById("summary").innerHTML = res['text']
});