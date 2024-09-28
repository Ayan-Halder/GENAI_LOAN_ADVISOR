from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from genai import generate_response  # Adjust this import if necessary

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("frontend/index.html") as f:
        return f.read()

@app.post("/generate")
async def get_ai_response(request: Request):
    data = await request.json()
    user_prompt = data.get("userPrompt")
    response = generate_response(user_prompt)
    return {"response": response}
