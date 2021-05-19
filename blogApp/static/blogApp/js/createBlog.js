function syncTitleAndSlug() {
  const slugInput = document.getElementById("slug-field")
  const titleInput = document.getElementById("title-field")

  slugInput.value = generateSlug(titleInput.value)
}

function generateSlug(title) {
  return title
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9ก-๙-]/gi, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
}

function configureEditorSize() {
  const editor = document.getElementById("cke_id_content")
  const widget = document.getElementsByClassName("django-ckeditor-widget")[0]

  widget.style = ""
  editor.style = ""
}

document.getElementById("title-field").onchange = function () {
  syncTitleAndSlug()
}

window.onload = function () {
  setTimeout(function () {
    configureEditorSize()
  }, 500)
}
