from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    """
    User Model - repräsentiert die 'users' Tabelle in der Datenbank.
    Erbt von Base, damit SQLAlchemy die Tabelle automatisch erstellt.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    
    
    # Relationships
    
    # Ein User kann Mitglied in mehreren Wallets sein
    wallet_members = relationship(
        "WalletMember",
        back_populates="user",
        cascade="all, delete-orphan" # cascade: wenn User gelöscht wird, werden auch seine WalletMember-Einträge gelöscht
    )
    
    # Ein User kann mehrere Expenses bezahlt haben
    # alle Ausgaben, die dieser User bezahlt hat
    expenses_paid = relationship(
        "Expense",
        back_populates="paid_by_user"
    )
    
    