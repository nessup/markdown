


function capture() {
	//alert("capturing");
    //alert($(document).hmtl())
 	chrome.tabs.captureVisibleTab(null, {format: "png"}, append);
    chrome.tabs.executeScript(null, {code:"document.body.bgColor='red'"});
    sleep(1000)
 	chrome.tabs.captureVisibleTab(null, {format: "png"}, append);
    chrome.tabs.executeScript(null, {code:"document.body.bgColor='blue'"});
    sleep(1000)
 	chrome.tabs.captureVisibleTab(null, {format: "png"}, append);
};

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function append(dataUrl){
	  content = document.getElementById('screenshots');
	  var image = document.createElement('img');
	  image.setAttribute('src', dataUrl);
	  content.appendChild(image);
}



   $("#capture").click(capture());

