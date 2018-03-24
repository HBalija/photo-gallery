var element = document.querySelector('.warning')
var image = document.querySelector('.image')

element.style.display = 'none'

image.addEventListener('click', function () {
  element.style.display === 'none' ? element.style.display = '' : element.style.display = 'none'
})
