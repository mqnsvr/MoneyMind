from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import auth, wallets, expenses, categories

from app.core.config import settings


# Initialize FastAPI app with name from settings
app = FastAPI(title=settings.app_name)



# Enable CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,  # Which origins can access the API
    allow_credentials=True,  # Allow cookies/auth headers (send things like JWT tokens)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/health")
def health_check():
    """Simple health check endpoint to verify API is running."""
    return {"status": "ok"}



app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(wallets.router, prefix="/api/v1/wallets", tags=["wallets"])
app.include_router(expenses.router, prefix="/api/v1/expenses", tags=["expenses"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])



# from google import genai
# import base64


# client = genai.Client(api_key="AIzaSyBvo46_UCxi5JMwEcO9RUZ1cu6buOrPHKQ")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)


