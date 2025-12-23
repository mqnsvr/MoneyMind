from typing import Optional
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel


class ExpenseBase(BaseModel):

    category_id: int
    amount: Decimal
    description: Optional[str] = None
    paid_at: Optional[datetime] = None
    
class ExpenseCreate(ExpenseBase):
    """Wird beim Anlegen einer Expense verwendet."""
    pass

class ExpenseUpdate(BaseModel):
    """Für Änderungen, alles optional."""
    category_id: Optional[int] = None
    amount: Optional[Decimal] = None
    description: Optional[str] = None
    paid_at: Optional[datetime] = None 
    
class ExpenseRead(ExpenseBase):
    """Was der Client zurückbekommt."""
    id: int
    wallet_id: int
    paid_by_id: int
    

    class Config:
        # erlaubt es, direkt ein SQLAlchemy-Objekt an FastAPI zu returnen. FastAPI baut daraus automatisch das Pydantic-Modell.
        from_attributes = True # Pydantic v2: wie früher orm_mode = True
        