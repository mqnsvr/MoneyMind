from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    type: str = "EXPENSE"  # or "INCOME"
    
class CategoryCreate(CategoryBase):
    """Wird beim Anlegen einer Category verwendet."""
    pass

class CategoryUpdate(BaseModel):
    """Für Änderungen, alles optional."""
    name: Optional[str] = None
    type: Optional[str] = None
    
class CategoryRead(CategoryBase):
    """Was der Client zurückbekommt."""
    id: int
    wallet_id: int
    

    class Config:
        # erlaubt es, direkt ein SQLAlchemy-Objekt an FastAPI zu returnen. FastAPI baut daraus automatisch das Pydantic-Modell.
        from_attributes = True # Pydantic v2: wie früher orm_mode = True