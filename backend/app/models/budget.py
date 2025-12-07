from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base

class Budget(Base):
    __tablename__ = "budgets"
    __table_args__ = (
        UniqueConstraint("wallet_id", "category_id", "month", name="uq_budget_wallet_cat_month"),
    )

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    # z.B. "2025-12"
    month = Column(String(7), nullable=False)
    limit_amount = Column(Numeric(12, 2), nullable=False)

    wallet = relationship("Wallet", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")
