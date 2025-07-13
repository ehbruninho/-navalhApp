document.addEventListener("DOMContentLoaded", function () {
    const toggleBtns = document.querySelectorAll(".toggle-password");

    toggleBtns.forEach(btn => {
        btn.addEventListener("click", function () {
            const input = this.closest(".input-group").querySelector("input");
            const icon = this.querySelector("i");

            if (input.type === "password") {
                input.type = "text";
                icon.classList.remove("fa-eye");
                icon.classList.add("fa-eye-slash");
            } else {
                input.type = "password";
                icon.classList.remove("fa-eye-slash");
                icon.classList.add("fa-eye");
            }
        });
    });
});
