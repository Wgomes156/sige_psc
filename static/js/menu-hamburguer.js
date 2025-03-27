document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector("nav ul");
    const iconOpen = document.getElementById('open');
    const iconClosed = document.getElementById('closed');

    menuToggle.addEventListener("click", function () {
        navMenu.classList.toggle("show");
        iconOpen.classList.toggle("noshow");
        iconClosed.classList.toggle("noshow");
    });
});
