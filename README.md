# Chatbot Backend

## Overview
This project is a backend service for a chatbot application, supporting real-time interactions and AI-powered responses. The backend is built using **Python (FastAPI/Flask)** and **Node.js (Express.js)** to provide flexibility in development and deployment. It integrates **GPT-3.5** for generating AI-based responses.

## Features
- Natural Language Processing (NLP) for chatbot responses
- **GPT-3.5 integration** for advanced AI-generated replies
- API integration with OpenAI/GPT models
- User authentication and session management
- WebSocket support for real-time chat
- Database storage for conversation history

## Technologies Used
- **Python** (FastAPI/Flask)
- **Node.js** (Express.js)
- **GPT-3.5** (OpenAI API)
- **MongoDB/PostgreSQL** for storing user data
- **WebSockets** for real-time chat
- **Docker** for containerized deployment

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js 16+
- MongoDB or PostgreSQL
- OpenAI API Key
- Docker (optional)

### Setup (Python)
```bash
# Clone the repository
git clone https://github.com/your-repo/chatbot-backend.git
cd chatbot-backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export OPENAI_API_KEY='your-api-key'

# Run the backend
uvicorn main:app --reload
```

### Setup (Node.js)
```bash
# Install dependencies
cd node-backend
npm install

# Set up environment variables
export OPENAI_API_KEY='your-api-key'

# Start the server
node server.js
```

## API Endpoints
### Python Backend (FastAPI/Flask)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/chat` | Send a message to GPT-3.5 and get a response |
| GET | `/history` | Get user chat history |

### Node.js Backend (Express.js)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/status` | Health check |
| POST | `/message` | Process a user message via GPT-3.5 |
| GET | `/logs` | Retrieve conversation logs |

## Deployment
### Using Docker
```bash
# Build and run the container
docker-compose up --build
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests and issues!

