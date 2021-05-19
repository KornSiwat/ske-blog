function hideSidebar(){
    let sidebar = document.getElementById("sidebar")
    let textSection = document.getElementById("text-section")
    let sidebarPos = sidebar.offsetTop+ window.pageYOffset
    let textSectionPos = textSection.offsetTop

    if (sidebarPos < textSectionPos) {
        sidebar.style.visibility = "hidden"
        sidebar.style.opacity = 0
    }   else if ( textSectionPos < sidebarPos && sidebarPos <= textSectionPos + textSection.offsetHeight - 150 ) {
        sidebar.style.visibility = "visible";
        sidebar.style.opacity = 1
    } else {
        sidebar.style.visibility = "hidden"
        sidebar.style.opacity = 0
    }
} 

var countScroll = 0

window.onscroll = function() { 
    hideSidebar()
};
