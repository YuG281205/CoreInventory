document.getElementById("loginForm").addEventListener("submit", function(e) {

    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("/api/login/", {

        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },

        body: JSON.stringify({ email, password })

    })

    .then(response => response.json())

    .then(data => {

        if(data.message){

            document.getElementById("message").style.color = "green";
            document.getElementById("message").innerText = data.message;

            window.location.href = "/api/dashboard/";

        } 
        else{

            document.getElementById("message").style.color = "red";
            document.getElementById("message").innerText = data.error || "Login failed";

        }

    })

    .catch(error => console.error("Error:", error));

});