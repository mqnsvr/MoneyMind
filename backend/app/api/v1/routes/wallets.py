from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.wallet import WalletCreate, WalletRead, WalletUpdate
from app.services.wallet_service import (
    get_wallet_by_id_for_user,
    create_wallet_for_user,
    update_wallet_for_user,
    delete_wallet_for_user,
    get_wallets_for_user,
    FAKE_CURRENT_USER_ID
)

router = APIRouter()

def get_fake_current_user_id() -> int:
    return FAKE_CURRENT_USER_ID

@router.post("/", response_model=List[WalletRead])
def list_wallets()