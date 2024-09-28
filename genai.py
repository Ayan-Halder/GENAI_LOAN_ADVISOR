import google.generativeai as genai
import os

# Configure the GenAI API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(user_prompt):
    try:
        response = model.generate_content(user_prompt)
        if response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return "No response from the bot."
    except Exception as e:
        return f"Error in AI generation: {str(e)}"
