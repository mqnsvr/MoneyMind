from os import access
import token
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from app.schemas.auth import Token
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.core.deps import get_db
from app.core.security import create_access_token, hash_password, verify_password
from app.core.deps import get_current_user


router = APIRouter()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. E-mail ist schon vorhanden?
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed = hash_password(user_in.password)
    
    user = User(
        email=user_in.email,
        hashed_password=hashed,
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
        
    
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password",
        )
    access_token = create_access_token(subject=user.email)
    return Token(access_token=access_token, token_type="bearer")
    
    
@router.get("/me", response_model=UserRead)
def read_current_user(
    current_user: User = Depends(get_current_user),
):
    """Gibt Informationen über den aktuell eingeloggten User zurück."""
    return current_user