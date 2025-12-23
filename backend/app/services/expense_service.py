from decimal import Decimal
from typing import Optional, List
from sqlalchemy.orm import Session
from datetime import date, datetime


from app.models.expense import Expense
from app.models.wallet import Wallet


def get_wallet_for_user(db: Session, wallet_id: int, user_id: int) -> Optional[Wallet]:
    """
    Retrieve all wallets for a given user.
    """
    return(
        db.query(Wallet)
        .filter(
            Wallet.id == wallet_id,
            Wallet.created_by_id == user_id)
        .first()
    )

def get_expense_by_id(
    db: Session,
    expense_id: int,
    wallet_id: int
    ) -> Optional[Expense]:
    return (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.wallet_id == wallet_id
        )
        .first()
    )


def get_expenses_for_wallet(
    db: Session, 
    wallet_id: int,
    user_id: int,
    start_date: Optional[date]=None,
    end_date: Optional[date]=None,
    category_id: Optional[int]=None
    ) -> List[Expense]:
    
    query = db.query(Expense).filter(Expense.wallet_id == wallet_id)
    
    if category_id is not None:
        query = query.filter(Expense.category_id == category_id)
    
    if start_date is not None:
        query = query.filter(Expense.paid_at >= datetime.combine(start_date, datetime.min.time()))
        
    if end_date is not None:
        query = query.filter(Expense.paid_at <= datetime.combine(end_date, datetime.max.time()))
    
    return query.all()

def create_expense_for_wallet(
    db: Session,
    wallet_id: int,
    user_id: int,
    amount: Decimal,
    description: Optional[str],
    category_id: int,
    paid_at: Optional[datetime]= None,
    ) -> Expense:
    expense = Expense(
        wallet_id=wallet_id,
        paid_by_id=user_id,
        amount=amount,
        description=description,
        category_id=category_id,
        paid_at=paid_at or datetime.utcnow()
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense
    

def update_expense(
    db: Session,
    expense: Expense,
    category_id: Optional[int],
    amount: Optional[Decimal],
    description: Optional[str],
    paid_at: Optional[datetime]
    ) -> Expense:
    if category_id is not None:
        expense.category_id = category_id
    if amount is not None:
        expense.amount = amount
    if description is not None:
        expense.description = description
    if paid_at is not None:
        expense.paid_at = paid_at
        
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def delete_expense(db: Session, expense: Expense) -> None:
    db.delete(expense)
    db.commit()