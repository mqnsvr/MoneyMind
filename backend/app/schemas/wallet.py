from pydantic import BaseModel
from typing import Optional

class WalletBase(BaseModel):
    """Base schema for Wallet."""

    name: str
    description: Optional[str] = None
    currency: str = "EUR"
    
class WalletCreate(WalletBase):
    """Daten, die der Client schicken muss, um eine Wallet zu erstellen."""
    pass

class WalletUpdate(BaseModel):
    """Daten, mit denen eine Wallet aktualisiert werden kann."""
    name: Optional[str] = None
    description: Optional[str] = None
    currency: Optional[str] = None
    
class WalletRead(WalletBase):
    """Daten, die wir dem Client zurückgeben."""
    id: int
    

    class Config:
        # erlaubt es, direkt ein SQLAlchemy-Objekt an FastAPI zu returnen. FastAPI baut daraus automatisch das Pydantic-Modell.
        from_attributes = True # Pydantic v2: wie früher orm_mode = True
        