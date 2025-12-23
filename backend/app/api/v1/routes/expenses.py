from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.expense import ExpenseRead, ExpenseCreate, ExpenseUpdate
from app.services.expense_service import (
    get_expense_by_id,
    get_expenses_for_wallet,
    create_expense_for_wallet,
    delete_expense,
    update_expense,
)
from app.core.deps import get_current_user, get_current_wallet_member
from app.models.user import User
from app.models.wallet_member import WalletMember


router = APIRouter()


@router.get("/wallets/{wallet_id}/expenses", response_model=List[ExpenseRead])
def list_expenses(
    wallet_id: int,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    category_id: Optional[int] = Query(None),
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """List all expenses for a wallet. User must be a member."""
    expenses = get_expenses_for_wallet(
        db,
        wallet_id=wallet_id,
        user_id=member.user_id,
        start_date=start_date,
        end_date=end_date,
        category_id=category_id,
    )
    return expenses


@router.post("/wallets/{wallet_id}/expenses", response_model=ExpenseRead, status_code=status.HTTP_201_CREATED)
def create_expense(
    wallet_id: int,
    expense_in: ExpenseCreate,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Create a new expense. User must be a member of the wallet."""
    expense = create_expense_for_wallet(
        db,
        wallet_id=wallet_id,
        user_id=member.user_id,
        amount=expense_in.amount,
        description=expense_in.description,
        category_id=expense_in.category_id,
        paid_at=expense_in.paid_at,
    )
    return expense


@router.put("/wallets/{wallet_id}/expenses/{expense_id}", response_model=ExpenseRead)
def update_expense_endpoint(
    wallet_id: int,
    expense_id: int,
    expense_in: ExpenseUpdate,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Update an expense. User must be a member of the wallet."""
    expense = get_expense_by_id(db, expense_id=expense_id, wallet_id=wallet_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    expense = update_expense(
        db,
        expense=expense,
        amount=expense_in.amount,
        description=expense_in.description,
        category_id=expense_in.category_id,
        paid_at=expense_in.paid_at,
    )
    return expense

@router.delete("/wallets/{wallet_id}/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense_endpoint(
    wallet_id: int,
    expense_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Delete an expense. User must be a member of the wallet."""
    expense = get_expense_by_id(db, expense_id=expense_id, wallet_id=wallet_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    delete_expense(db, expense=expense)
    return None