from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI  # Import the new OpenAI client

# Load environment variables from the .env file
load_dotenv()

# Debug: Print the API key to verify it's loaded correctly
print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Enable CORS for all origins (adjust as needed for your deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    user_input: str

# Establish database connection
try:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cursor = conn.cursor()
except Exception as e:
    raise Exception("Database connection failed: " + str(e))

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Health-check endpoint
@app.get("/")
def read_root():
    return {"message": "Chatbot API is running"}

# Chat endpoint
@app.post("/chat/")
def chat(request: ChatRequest):
    user_input = request.user_input

    try:
        # Generate a response using OpenAI's GPT-3.5-turbo
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the new model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.7
        )
        bot_response = response.choices[0].message.content.strip()

        # Insert the conversation into the database
        cursor.execute(
            "INSERT INTO chatbot_logs (user_input, bot_response) VALUES (%s, %s)",
            (user_input, bot_response)
        )
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: " + str(e))

    return {"user_input": user_input, "reply": bot_response}