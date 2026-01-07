//functions 

function toggleMenu() {
    menu.classList.toggle('active');
}


// The navigation menu 


//getting the elements
const button = document.getElementById('hamburger');
const menu = document.getElementById('navbar')

//eventlisteners 
button.addEventListener('click', toggleMenu);