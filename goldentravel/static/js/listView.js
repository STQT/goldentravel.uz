
window.addEventListener("scroll", function() {
    var navbar = document.querySelector('nav')
    navbar.classList.toggle('sticky', window.scrollY > 0)
})

$(document).ready(function(){
    $(".container .slides img").click(function(){
        var $smallImages = $(this).attr('src')
        $(".big-screen img").attr("src", $smallImages);
    })
})
$(document).ready(function(){
    $(".container1 .slides1 img").click(function(){
        var $smallImages = $(this).attr('src')
        $(".big-screen1 img").attr("src", $smallImages);
    })
})

// var modalBtn=document.querySelector('.modal-btn')
// var modalBg=document.querySelector('.modal-bg')
// var modalClose=document.querySelector(".modal-close")
// modalBtn.addEventListener("click", function(){
//     modalBg.classList.add("bg-active")
// })
// modalClose.addEventListener("click", function(){
//     modalBg.classList.remove("bg-active")
// })


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
