from typing import Optional, List
from sqlalchemy.orm import Session

from app.models.wallet import Wallet
from app.models.wallet_member import WalletMember


def get_wallets_for_user(db: Session, user_id: int) -> List[Wallet]:
    """
    Retrieve all wallets for a given user.
    """
    return(
        db.query(Wallet)
        .filter(Wallet.created_by_id == user_id)
        .all()
    )
    
def get_wallet_by_id_for_user(
    db: Session, wallet_id: int, user_id: int
) -> Optional[Wallet]:
    """
    Retrieve a specific wallet by its ID for a given user.
    """
    return (
        db.query(Wallet)
        .filter(
            Wallet.id == wallet_id,
            Wallet.created_by_id == user_id
        )
        .first()
    )
    
def create_wallet_for_user(db:Session, user_id: int, name: str, description: str | None, currency: str) -> Wallet:
    """
    Create a new wallet for a given user.
    Also creates a WalletMember entry with OWNER role.
    """
    # 1. Create the wallet
    wallet = Wallet(
        name=name,
        description=description,
        currency=currency,
        created_by_id=user_id
    )
    db.add(wallet)
    db.flush()  # Get the wallet.id without committing
    
    # 2. Create WalletMember entry so user can access the wallet
    member = WalletMember(
        wallet_id=wallet.id,
        user_id=user_id,
        role="OWNER"
    )
    db.add(member)
    
    db.commit()
    db.refresh(wallet)
    return wallet

def update_wallet_for_user(db: Session, wallet: Wallet, name: str | None, description: str | None, currency: str | None) -> Wallet:
    if name is not None:
        wallet.name = name
    if description is not None:
        wallet.description = description
    if currency is not None:
        wallet.currency = currency

    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet

def delete_wallet_for_user(db: Session, wallet: Wallet) -> None:
    db.delete(wallet)
    db.commit()