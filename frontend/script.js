const form = document.getElementById("complaintForm");
const message = document.getElementById("message");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const complaint =
        document.getElementById("complaint").value;

    const location =
        document.getElementById("location").value;

    const image =
        document.getElementById("image").files[0];

    const logoutButton = document.getElementById("logoutButton");

    if (logoutButton) {
        logoutButton.addEventListener("click", function () {
            localStorage.removeItem("loggedInUser");
            window.location.href = "login.html";
        });
    }


    // Get logged-in user
    const storedUser =
        localStorage.getItem("loggedInUser");

    if (!storedUser) {

        alert("Please login first.");

        window.location.href = "login.html";

        return;
    }

    const user =
        JSON.parse(storedUser);


    // Create FormData
    const formData = new FormData();

    formData.append("complaint", complaint);
    formData.append("location", location);

    formData.append("user_id", user.id);
    formData.append("user_email", user.email);

    if (image) {
        formData.append("image", image);
    }


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/complaints",
            {
                method: "POST",
                body: formData
            }
        );


        const result = await response.json();

        console.log("Server Response:", result);

        message.textContent = result.message;

        form.reset();

    } catch (error) {

        console.error("Error:", error);

        message.textContent =
            "Unable to submit complaint.";
    }

});

// Logout button
const logoutButton = document.getElementById("logoutButton");

if (logoutButton) {
    logoutButton.addEventListener("click", function () {
        localStorage.removeItem("loggedInUser");
        window.location.href = "login.html";
    });
}