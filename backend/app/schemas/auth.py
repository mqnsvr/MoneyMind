from pydantic import BaseModel

class Token(BaseModel):
    """Schema für das Access Token, das an den Client zurückgegeben wird."""
    access_token: str
    token_type: str = "bearer"  # üblicherweise "bearer" für JWTs