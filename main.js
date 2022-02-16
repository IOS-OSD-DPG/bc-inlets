function clearContent(kind) {
	var i;
	var contentClass = kind + "-content";
	var tablinkClass = kind + "-tablinks";

	var content = document.getElementsByClassName(contentClass);
	for (i = 0; i < content.length; i++) {
		content[i].style.display = "none";
	}

	var tablinks = document.getElementsByClassName(tablinkClass);
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active", "");
	}
}

function changeAveraging(event, averaging) {
	var i;

	clearContent("averaging")

	var showContent = document.getElementsByClassName(averaging);
	for (i = 0; i < showContent.length; i++) {
		showContent[i].style.display = "block";
	}
	event.currentTarget.className += " active";
}

function changeInlet(event, inlet) {
	var i;

	clearContent("inlet")

	document.getElementById(inlet).style.display = "block";
	event.currentTarget.className += " active";
}

document.getElementById("averaging-default").click();
document.getElementById("inlet-default").click();
