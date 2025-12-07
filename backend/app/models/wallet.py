from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Wallet(Base):
    """
    Wallet Model - repräsentiert die 'wallets' Tabelle in der Datenbank.
    Ein Wallet ist eine gemeinsame Geldbörse (z.B. WG, Urlaub, Paar).
    """
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    currency = Column(String(10), default="EUR")
    
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    created_by = relationship("User")
    
    members = relationship(
        "WalletMember", 
        back_populates="wallet", 
        cascade="all, delete-orphan"
    )
    categories = relationship(
        "Category",
        back_populates="wallet",
        cascade="all, delete-orphan"
    )
    budgets = relationship(
        "Budget",
        back_populates="wallet",
        cascade="all, delete-orphan"
    )
    expenses = relationship(
        "Expense",
        back_populates="wallet",
        cascade="all, delete-orphan"
    )