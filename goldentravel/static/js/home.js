window.addEventListener("scroll", function() {
    var navbar = document.querySelector('nav')
    navbar.classList.toggle('sticky', window.scrollY > 0)
})

console.log('salom');

// -------------------------------------------


var bars = document.querySelector('.bars')
var list = document.querySelector('.list')

setTimeout(() => {
    bars.addEventListener('click', () => {
        list.classList.add('add')
    })
},100);

// ------------------------------------------------

var delete1 = document.querySelector('.delete')

delete1.addEventListener('click', () => {
        list.style.display = 'none'
})