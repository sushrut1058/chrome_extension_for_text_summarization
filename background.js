const socket = new WebSocket('ws://localhost:3000');
// Connection opened
socket.addEventListener('open', function (event) {
	console.log('Connected to the WS Server!')
});

chrome.contextMenus.create({
	id:"1",
	title: "Summarize: %s",
	contexts: ["selection"]
})

chrome.contextMenus.onClicked.addListener(function(info){	
    chrome.storage.sync.set({'text':'Loading...'},function(){})
    socket.send(info["selectionText"]);	
    socket.addEventListener('message', function (event) {
        chrome.storage.sync.set({'text':event.data},function(){})
    });

	
})