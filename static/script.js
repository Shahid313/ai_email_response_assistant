function generateResponse() {
    const email = document.getElementById("emailInput").value;
    const tone = document.getElementById("toneSelect").value;
    const loader = document.getElementById("loader");
    const responseBox = document.getElementById("responseBox");

    responseBox.innerText = "";
    loader.style.display = "inline-block"; // show spinner

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email, tone: tone })
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = "none"; // hide spinner
        responseBox.innerText = data.response;
    })
    .catch(error => {
        loader.style.display = "none"; // hide spinner
        responseBox.innerText = "Error: " + error.message;
    });
}
