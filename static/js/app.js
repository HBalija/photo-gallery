// vanilla JS CODE

var links = document.querySelectorAll('#imageGallery a')

var overlay = document.createElement('div')
overlay.id = 'overlay'

var image = document.createElement('img')
var caption = document.createElement('p')

overlay.appendChild(image)
overlay.appendChild(caption)

document.body.appendChild(overlay)

links.forEach(function (link) {
  link.addEventListener('click', function (event) {
    event.preventDefault()

    var imageLocation = this.attributes.href.textContent
    image.setAttribute('src', imageLocation)

    overlay.style.display = 'block'

    var captionText = this.querySelector('img').alt
    overlay.querySelector('p').textContent = captionText
  })
})

overlay.addEventListener('click', function () {
  this.style.display = 'none'
})

$('#overlay').height($(document).height());

/*
// jQuery code (include jQuery in index.html)

var $overlay = $('<div id="overlay"></div>')
var $image = $('<img>')
var $caption = $('<p></p>')

$overlay.append($image)
$overlay.append($caption)

$('body').append($overlay)

$('#imageGallery a').click(function (event) {
  event.preventDefault()
  var imageLocation = $(this).attr('href')
  $image.attr('src', imageLocation)

  $overlay.show()

  var captionText = $(this).children('img').attr('alt')
  $caption.text(captionText)
})

$overlay.click(function () {
  $overlay.hide()
})

*/
