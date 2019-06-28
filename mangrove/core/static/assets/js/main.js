nb = document.getElementById("nav-fixed")

window.onscroll = function (oEvent) {
	if (window.pageYOffset > (screen.height / 2)){
		nb.classList.add("nav-fixed");
    } else {
        nb.classList.remove("nav-fixed");
    }
}