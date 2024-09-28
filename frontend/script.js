// script.js

document.getElementById("loan-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const loanAmount = document.getElementById("loanAmount").value;
    const loanPurpose = document.getElementById("loanPurpose").value;
    const customPurpose = document.getElementById("customPurpose").value;
    const income = document.getElementById("income").value;
    const responseContainer = document.getElementById("response-container");

    responseContainer.innerHTML = "Loading...";

    try {
        const response = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                userPrompt: `Name: ${name}, Loan Amount: ${loanAmount}, Purpose: ${loanPurpose === 'other' ? customPurpose : loanPurpose}, Annual Income: ${income}`
            }),
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        responseContainer.innerHTML = data.response || "No response from the AI.";
    } catch (error) {
        responseContainer.innerHTML = `Error: ${error.message}`;
    }
});
