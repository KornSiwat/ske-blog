function showSlides() {
  let slides = document.getElementsByClassName("mySlides")
  let dots = document.getElementsByClassName("dot")

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none"
  }

  slideIndex++

  if (slideIndex > slides.length) {
    slideIndex = 1
  }

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "")
  }

  slides[slideIndex - 1].style.display = "block"
  dots[slideIndex - 1].className += " active"
  setTimeout(showSlides, 4000) // Change image every 2 seconds
}

function configBannerSize() {
  const hasSponsorBanner =
    Array.from(document.getElementsByClassName("sponsor-banner")).length !== 0

  const mainBannerContainer = document.getElementsByClassName(
    "main-banner-container"
  )[0]

  const sponsorBannerContainer = document.getElementsByClassName(
    "sponsor-banner-container"
  )[0]

  if (!hasSponsorBanner) {
    mainBannerContainer.style.width = "100%"
    sponsorBannerContainer.style.width = "0"
  }
}

window.onload = function () {
  configBannerSize()
}

let slideIndex = 0
showSlides()
