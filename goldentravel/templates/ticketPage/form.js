var form = document.querySelector('#input')
var btn = document.querySelector('#btn')
var div = document.querySelector('.div')
var label = document.querySelector('.form-check-label')


form.addEventListener('click', () => {
    btn.style.display = 'block'
    // btn.style.marginLeft = '490px'
})

label.addEventListener('click', () => {
    btn.style.display = 'block'
    // btn.style.marginLeft = '500px'
})