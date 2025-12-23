from enum import member
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User
from app.models.wallet_member import WalletMember

# 1. FastAPI weiß, wo ma den Token im Request findet (Login-Endpoint)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Liest JWT aus dem Header, dekodiert ihn und lädt den User aus der DB."""
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try: 
        # 2. JWT dekodieren
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
        sub: str | None = payload.get("sub")
        if sub is None:
            raise cred_exc
    except JWTError:
        # Token ungültig, abgelaufen oder manipuliert.
        raise cred_exc
    
    # 3. user zu diesem subject (z.B email) laden
    user = db.query(User).filter(User.email == sub).first()
    if not user:
        raise cred_exc
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
        )
        
    return user

def get_current_wallet_member(
    wallet_id: int,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db),
) -> WalletMember:
    """Prüft, ob der aktuelle User Mitglied dieser Wallet ist.
    Gibt  das WalletMember-Objekt zurück (inkl. Rolle)
    """
    
    member = (
        db.query(WalletMember)
        .filter(WalletMember.wallet_id == wallet_id,
                WalletMember.user_id == current_user.id)
        .first()
    )
    if not member:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not a member of this wallet",
        )
    return member

    