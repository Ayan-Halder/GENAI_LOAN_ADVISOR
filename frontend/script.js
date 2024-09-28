document.getElementById("loanForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);
    const data = {
        loan_type: formData.get("loanType"),
        credit_score: parseInt(formData.get("creditScore")),
        loan_term: parseInt(formData.get("loanTerm")),
        existing_debt: parseFloat(formData.get("existingDebt")),
        preferred_lending_institution: formData.get("preferredInstitution"),
        annual_income: parseFloat(formData.get("annualIncome")),
        loan_amount_requested: parseFloat(formData.get("loanAmountRequested")),
    };

    // Send the data to the backend
    const response = await fetch("/generate-advice", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    
    // Display the advice received from the backend
    document.getElementById("adviceOutput").innerText = result.advice;
});
