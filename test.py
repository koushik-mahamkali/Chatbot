from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Test the API key
try:
    response = client.completions.create(
        model="text-davinci-003",
        prompt="What is the capital of France?",
        max_tokens=50
    )
    print("API Key is valid. Response:", response.choices[0].text.strip())
except Exception as e:
    print("Error:", e)