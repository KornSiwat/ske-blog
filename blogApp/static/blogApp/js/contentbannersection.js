function contentShowSlides() {
    let contentSlides = document.getElementsByClassName("content-mySlides");

    for (let i = 0; i < contentSlides.length; i++) {
      contentSlides[i].style.display = "none";  
    }

    contentSlideIndex++

    console.log(contentSlideIndex)

    if (contentSlideIndex > contentSlides.length) {
      contentSlideIndex = 1
    }

    contentSlides[contentSlideIndex-1].style.display = "block";  

    setTimeout(contentShowSlides, 5000)
}

let contentSlideIndex = 0;
contentShowSlides()