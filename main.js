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

function changeAveraging(event) {
	var i;
	var target = event.currentTarget;
	var averaging = target.id;

	clearContent("averaging")

	var showContent = document.getElementsByClassName(averaging);
	for (i = 0; i < showContent.length; i++) {
		showContent[i].style.display = "block";
	}
	target.className += " active";

	window.sessionStorage.setItem("averaging", averaging)
}

function changeInlet(event) {
	var i;
	var target = event.currentTarget;
	var inlet = target.id;

	clearContent("inlet")

	document.getElementById(inlet + "-content").style.display = "block";
	target.className += " active";

	window.sessionStorage.setItem("inlet", inlet)
}

if (window.sessionStorage.getItem("averaging")) {
	document.getElementById(window.sessionStorage.getItem("averaging")).click();
} else {
	// choose default
	document.getElementById("monthly").click();
}
if (window.sessionStorage.getItem("inlet")) {
	document.getElementById(window.sessionStorage.getItem("inlet")).click();
} else {
	// choose default
	document.getElementById("saanich-inlet").click();
}
