// This function is triggered when the button is clicked
async function sendData() {
    // Get the value from the input box
    const text = document.getElementById("input-text").value;

    // Send a POST request tot he Python backend
    const response = await fetch("http://localhost:8000/send-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" // Telling the backend we're sending JSON data
        },
        body: JSON.stringify({
            text: text  // Convert the text to JSON format
        })
    });

    // Wait for the response from Python and convert it to JSON
    const data = await response.json();

    // Display the response from Python in the <p> tag
    document.getElementById("response").innerText = data.message;
}