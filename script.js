document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault();
        alert("Your request has been submitted!");
    });
});

function scrollToForm() {
    document.getElementById("contact").scrollIntoView({ behavior: "smooth" });
}