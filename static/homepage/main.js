// Show menu
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)

    if (toggle && nav) {
        toggle.addEventListener("click", () => {
            nav.classList.toggle("show")
            console.log(nav)
        })
    }
}
showMenu("nav-toggle", "nav-menu")


const navLink = document.querySelectorAll(".nav_link");

function linkAction() {
    navLink.forEach(n => n.classList.remove("active"));
    this.classList.add("active");

    const navMenu = document.getElementById("nav-menu")
    navMenu.classList.remove("show")
}
navLink.forEach(n => n.addEventListener("click", linkAction));


// Scroll reveal config
const sr = ScrollReveal({
    origin: "top",
    distance: "80px",
    duration: 2000,
    reset: true
});

sr.reveal(".home_title", {});
sr.reveal(".home_social-icon", { interval: 200 });
sr.reveal(".button", { delay: 200 });