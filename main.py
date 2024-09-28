from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from genai import generate_response  # Import the generate_response function
import os

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (frontend)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

class LoanData(BaseModel):
    loan_type: str
    credit_score: int
    loan_term: int
    existing_debt: float
    preferred_lending_institution: str
    annual_income: float
    loan_amount_requested: float

@app.post("/generate-advice")
async def generate_advice(data: LoanData):
    user_prompt = (
        f"Loan Type: {data.loan_type}\n"
        f"Credit Score: {data.credit_score}\n"
        f"Loan Term: {data.loan_term}\n"
        f"Existing Debt: {data.existing_debt}\n"
        f"Preferred Institution: {data.preferred_lending_institution}\n"
        f"Annual Income: {data.annual_income}\n"
        f"Loan Amount Requested: {data.loan_amount_requested}"
    )
    
    advice = generate_response(user_prompt)
    return {"advice": advice}

@app.get("/")
async def get_index():
    return FileResponse("frontend/index.html")

