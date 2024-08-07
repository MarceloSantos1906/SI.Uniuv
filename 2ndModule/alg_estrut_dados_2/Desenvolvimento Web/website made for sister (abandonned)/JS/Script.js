document.addEventListener('contextmenu', event => event.preventDefault());

function toggleMoreInfoAuriculo() {
    var auriculo = document.querySelector('.auriculo');
    auriculo.classList.toggle('show');
    var elem = document.getElementById("more_info_auriculo");
    if (elem.value == "MAIS INFORMAÇÕES") elem.value = "MENOS INFORMAÇÕES";
    else elem.value = "MAIS INFORMAÇÕES";
}

function toggleMoreInfoPilates() {
    var auriculo = document.querySelector('.pilates');
    auriculo.classList.toggle('show');
    var elem = document.getElementById("more_info_pilates");
    if (elem.value == "MAIS INFORMAÇÕES") elem.value = "MENOS INFORMAÇÕES";
    else elem.value = "MAIS INFORMAÇÕES";
}

function toggleMoreInfoQuiro() {
    var auriculo = document.querySelector('.quiro');
    auriculo.classList.toggle('show');
    var elem = document.getElementById("more_info_quiro");
    if (elem.value == "MAIS INFORMAÇÕES") elem.value = "MENOS INFORMAÇÕES";
    else elem.value = "MAIS INFORMAÇÕES";
}

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

setInterval(() => {
    plusSlides(1);
}, 4000);









