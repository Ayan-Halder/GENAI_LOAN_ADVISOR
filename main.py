from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from genai import generate_response  # Import the generate_response function

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
    name: str
    age: int
    loan_type: str
    credit_score: int
    loan_term: int
    existing_debt: float
    preferred_lending_institution: str
    annual_income: float
    loan_amount_requested: float
    currency: str
    country: str

@app.post("/generate-advice")
async def generate_advice(data: LoanData):
    user_prompt = (
        f"Provide a concise breakdown for my loan application, my name is {data.name}'s . "
        f"Age: {data.age}, Loan Type: {data.loan_type}, Credit Score: {data.credit_score}, "
        f"Loan Term: {data.loan_term} years, Existing Debt: {data.existing_debt}, "
        f"Preferred Institution: {data.preferred_lending_institution}, "
        f"Annual Income: {data.annual_income}, Loan Amount Requested: {data.loan_amount_requested}, "
        f"Currency: {data.currency}, Country: {data.country}. "
        f"Please list strengths, potential challenges, next steps, and important considerations using bullet points, and also give me a list of documents needed and suggested banks to consider"
    )
    
    advice = generate_response(user_prompt)
    return {"advice": advice}

@app.get("/")
async def get_index():
    return FileResponse("frontend/index.html")
