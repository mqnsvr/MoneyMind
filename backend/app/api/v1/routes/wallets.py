from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from httpx import get
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.wallet import WalletCreate, WalletRead, WalletUpdate
from app.services.wallet_service import (
    get_wallet_by_id_for_user,
    create_wallet_for_user,
    update_wallet_for_user,
    delete_wallet_for_user,
    get_wallets_for_user,
)
from app.core.deps import get_current_user, get_current_wallet_member
from app.models.user import User
from app.models.wallet_member import WalletMember
from app.models.wallet import Wallet

router = APIRouter()


@router.get("/", response_model=List[WalletRead])
def list_wallets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    wallets = (db.query(Wallet)
               .join(WalletMember, WalletMember.wallet_id == Wallet.id)
               .filter(WalletMember.user_id == current_user.id)
               .all()
    )
    return wallets

@router.post("/", response_model=WalletRead, status_code=status.HTTP_201_CREATED)
def create_wallet(
    wallet_in: WalletCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Erstelle eine neue Wallet für den aktuell eingeloggten User.
    Der User wird normalerweise als OWNER in WalletMember ein.
    """
    wallet = create_wallet_for_user(
        db,
        user_id=current_user.id,
        name=wallet_in.name,
        description=wallet_in.description,
        currency=wallet_in.currency,
    )
    return wallet

@router.get("/{wallet_id}", response_model=WalletRead)
def get_wallet(
    wallet_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """
    Hole eine einzelne Wallet, sofern der aktuelle User Mitglied ist.
    get_current_wallet_member stellt sicher, dass der User Zugriff hat.
    """
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.put("/{wallet_id}", response_model=WalletRead)
def update_wallet(
    wallet_id: int,
    wallet_in: WalletUpdate,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Update wallet. User muss Mitglied sein."""
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    wallet = update_wallet_for_user(
        db,
        wallet=wallet,
        name=wallet_in.name,
        description=wallet_in.description,
        currency=wallet_in.currency,
    )
    return wallet

@router.delete("/{wallet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wallet(
    wallet_id: int,
    db: Session = Depends(get_db),
    member: WalletMember = Depends(get_current_wallet_member),
):
    """Delete wallet. User muss Mitglied sein."""
    wallet = db.query(Wallet).filter(Wallet.id == wallet_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    delete_wallet_for_user(db, wallet=wallet)
    return None