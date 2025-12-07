from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    paid_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Numeric(12, 2), nullable=False)
    description = Column(String(255), nullable=True)
    paid_at = Column(DateTime, default=datetime.utcnow)

    wallet = relationship("Wallet", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
    paid_by_user = relationship("User", back_populates="expenses_paid")
