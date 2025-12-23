from multiprocessing.util import is_abstract_socket_namespace
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Base schema for User."""
    email: EmailStr
    is_active: bool = True
    
class UserCreate(UserBase):
    """Daten, die der Client schicken muss, um einen User zu erstellen."""
    email: EmailStr
    password: str # Klartext-Passwort, nur für die Anfrage. Wird später gehashed.
    
    
class UserRead(UserBase):
    """Daten, die wir dem Client zurückgeben."""
    id: int

    class Config:
        # erlaubt es, direkt ein SQLAlchemy-Objekt an FastAPI zu returnen. FastAPI baut daraus automatisch das Pydantic-Modell.
        from_attributes = True # Pydantic v2: wie früher orm_mode = True