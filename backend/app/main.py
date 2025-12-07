from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

# Initialize FastAPI app with name from settings
app = FastAPI(title=settings.app_name)

# Allowed origins for CORS (Cross-Origin Resource Sharing)
# Frontend dev server runs on port 5174 (Vite default)
origins = [
    "http://localhost:5174",
    "http://127.0.0.1:5174"
]

# Enable CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Which origins can access the API
    allow_credentials=True,  # Allow cookies/auth headers (send things like JWT tokens)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/health")
def health_check():
    """Simple health check endpoint to verify API is running."""
    return {"status": "ok"}




from google import genai
import base64


client = genai.Client(api_key="AIzaSyBvo46_UCxi5JMwEcO9RUZ1cu6buOrPHKQ")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)


