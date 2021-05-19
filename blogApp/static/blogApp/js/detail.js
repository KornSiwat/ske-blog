function getMaxWidth() {
  const container = document.getElementsByClassName("card-body")[0]
  const maxWidth = container.clientWidth

  return maxWidth
}

function configureImageSize() {
  const images = Array.from(document.getElementsByTagName("img"))
  const maxImageWidth = getMaxWidth()

  images.forEach((image) => {
    if (image.clientWidth > maxImageWidth) {
      image.style = `width:90%; height:auto;`
    }
  })
}

function configureVideoSize() {
  const iframes = Array.from(document.getElementsByTagName("iframe"))
  const maxVideoWidth = getMaxWidth()

  iframes.forEach((iframe) => {
    const currentHeight = iframe.height
    const currentWidth = iframe.width
    const heightWidthRatio = currentHeight / currentWidth
    const newWidth = 0.9 * maxVideoWidth
    const newHeight = newWidth * heightWidthRatio

    iframe.height = newHeight
    iframe.width = newWidth
    iframe.allowFullscreen = 'true'
  })
}

window.onload = function () {
  configureVideoSize()
  configureImageSize()
}

window.onresize = function () {
  configureVideoSize()
  configureImageSize()
}


