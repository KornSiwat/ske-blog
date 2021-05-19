function configCardContainerLayout() {
  const cardContainer = document.getElementsByClassName(
    "card-container"
  )[0]
  const cardsCount = document.getElementsByClassName("card").length
  const cardWidth = document.getElementsByClassName("card")[0].clientWidth + 20
  const cardsPerRow = Math.floor(cardContainer.clientWidth / cardWidth)
  const toBeAddedCardsCount = cardsPerRow - (cardsCount % cardsPerRow)

  if (cardsCount === 0) {
    return
  }

  deleteDummyCards()

  for (let i = 0; i < toBeAddedCardsCount; i++) {
    const dummyCard = document.createElement("div")
    dummyCard.className = "card dummy-card"

    cardContainer.append(dummyCard)
  }
}

function deleteDummyCards() {
  const dummyCards = Array.from(document.getElementsByClassName("dummy-card"))

  dummyCards.forEach((x) => x.remove())
}

configCardContainerLayout()
