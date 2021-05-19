function configScrollButtons() {
  const contentContainers = getContentContainers()

  contentContainers.forEach((contentContaner) => {
    if (!isElementOverflown(contentContaner)) {
      const scrollButtonContainers = Array.from(
        contentContaner.parentElement.children
      ).filter((x) => x.className.includes("content-scroll-button-container"))

      scrollButtonContainers.forEach((scrollButtonContainer) => {
        scrollButtonContainer.style.display = "none"
      })
    }
  })
}

function isElementOverflown(element) {
  return (
    element.scrollHeight > element.clientHeight ||
    element.scrollWidth > element.clientWidth
  )
}

function getContentContainers() {
  return Array.from(document.getElementsByClassName("content-container"))
}

function onLeftScrollButtonClicked(element) {
  const contentSection = element.parentElement.children[2]
  const xPosRaw = contentSection.scrollLeft - contentSection.clientWidth
  const xPosRounded = xPosRaw + (xPosRaw % 258)

  contentSection.scroll({
    left: xPosRounded,
    behavior: "smooth",
  })
}

function onRightScrollButtonClicked(element) {
  const contentSection = element.parentElement.children[2]
  const xPosRaw = contentSection.scrollLeft + contentSection.clientWidth
  const xPosRounded = xPosRaw - (xPosRaw % 258)

  contentSection.scroll({
    left: xPosRounded,
    behavior: "smooth",
  })
}

configScrollButtons()

window.onresize = function () {
  configScrollButtons()
}
