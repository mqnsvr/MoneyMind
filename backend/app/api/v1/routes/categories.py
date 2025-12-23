from typing import List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status

from app.db.session import get_db
from app.schemas.category import CategoryRead, CategoryCreate, CategoryUpdate
from app.services.category_service import (
    get_categories_for_wallet,
    get_category_by_id_for_wallet,
    create_category_for_wallet,
    update_category,
    delete_category,
)
from app.core.deps import get_current_wallet_member
from app.models.wallet_member import WalletMember


router = APIRouter()


@router.get("/wallets/{wallet_id}/categories", response_model=List[CategoryRead])
def list_categories(
    wallet_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """List all categories for a wallet. User must be a member."""
    categories = get_categories_for_wallet(db, wallet_id=wallet_id)
    return categories   

@router.post("/wallets/{wallet_id}/categories", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(
    wallet_id: int,
    category_in: CategoryCreate,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Create a new category. User must be a member of the wallet."""
    category = create_category_for_wallet(
        db,
        wallet_id=wallet_id,
        name=category_in.name,
        type=category_in.type,
    )
    return category

@router.get("/wallets/{wallet_id}/categories/{category_id}", response_model=CategoryRead)
def get_category(
    wallet_id: int,
    category_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Get a single category. User must be a member of the wallet."""
    category = get_category_by_id_for_wallet(
        db, category_id=category_id, wallet_id=wallet_id
    )
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/wallets/{wallet_id}/categories/{category_id}", response_model=CategoryRead)
def update_category_endpoint(
    wallet_id: int,
    category_id: int,
    category_in: CategoryUpdate,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Update a category. User must be a member of the wallet."""
    category = get_category_by_id_for_wallet(
        db, category_id=category_id, wallet_id=wallet_id
    )
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category = update_category(
        db,
        category=category,
        name=category_in.name,
        type=category_in.type,
    )
    return category

@router.delete("/wallets/{wallet_id}/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category_endpoint(
    wallet_id: int,
    category_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Delete a category. User must be a member of the wallet."""
    category = get_category_by_id_for_wallet(
        db, category_id=category_id, wallet_id=wallet_id
    )
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    delete_category(db, category=category)
    return None