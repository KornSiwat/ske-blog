function configureTagify() {
  const tagInput = document.getElementsByClassName("tagify--input")[0]

  tagInput.setAttribute("data-placeholder", "Add Tags")
  tagInput.setAttribute("pattern", "^[a-zA-Zก-๙0-9äöüÄÖÜ,]*$")
}

configureTagify()
