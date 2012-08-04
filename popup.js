


function capture() {
	alert("capturing");
 	chrome.tabs.captureVisibleTab(null, function(dataUrl) {
	  content = document.getElementById('screenshots');
	  var image = document.createElement('img');
	  image.setAttribute('src', dataUrl);
	  content.appendChild(image);
    });
};


   $("#capture").click(capture());

