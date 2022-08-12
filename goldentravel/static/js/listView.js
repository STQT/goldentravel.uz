
window.addEventListener("scroll", function() {
    var navbar = document.querySelector('nav')
    navbar.classList.toggle('sticky', window.scrollY > 0)
})

$(document).ready(function(){
    $(".container .row .slides img").click(function(){
        var $smallImages = $(this).attr('src')
        $(".container .row .image-row .big-screen img").attr("src", $smallImages);
    })
})
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
