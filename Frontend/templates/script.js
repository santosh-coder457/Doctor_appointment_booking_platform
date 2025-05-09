document.addEventListener("DOMContentLoaded", function () {
    // Select all "Book Appointment" buttons
    const bookButtons = document.querySelectorAll(".book-appointment");

    bookButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Get the doctor's name from the button's data attribute
            const doctorName = this.getAttribute("data-doctor");

            // Store the doctor's name in Local Storage
            localStorage.setItem("selectedDoctor", doctorName);
        });
    });
});
