from typing import Optional, List
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.wallet import Wallet
from app.services.wallet_service import get_wallet_by_id_for_user


def get_categories_for_wallet(db:Session, wallet_id: int) -> List[Category]:
    """
    Retrieve all categories for a given wallet.
    """
    return(
        db.query(Category)
        .filter(Category.wallet_id == wallet_id)
        .all()
    )
    
def get_category_by_id_for_wallet(
    db: Session, category_id: int, wallet_id: int
) -> Optional[Category]:
    """
    Retrieve a specific category by its ID for a given wallet.
    """
    return (
        db.query(Category)
        .filter(
            Category.id == category_id,
            Category.wallet_id == wallet_id
        )
        .first()
    )
    
def create_category_for_wallet(db:Session, wallet_id: int, name: str, type: str) -> Category:
    """ Create a new category for a given wallet."""
    category = Category(
        name=name,
        type=type,
        wallet_id=wallet_id
    )
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db:Session, category: Category, name: Optional[str], type: Optional[str]) -> Category:
    
    if name is not None:
        category.name = name
    if type is not None:
        category.type = type
        
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db:Session, category: Category) -> None:
    db.delete(category)
    db.commit()