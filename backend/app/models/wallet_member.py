from sqlalchemy import Integer, String, Text, ForeignKey, UniqueConstraint, Column
from sqlalchemy.orm import relationship

from app.db.base import Base

class WalletMember(Base):
    """
    WalletMember Model - repräsentiert die 'wallet_members' Tabelle in der Datenbank.
    Verbindet Users mit Wallets (Viele-zu-Viele Beziehung).
    """
    __tablename__ = "wallet_members"
    __table_args__ = (
        UniqueConstraint('user_id', 'wallet_id', name='uix_user_wallet'),
    )

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("wallets.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String(20), nullable=False, default="MEMBER")  # z.B. 'admin', 'member'
    

    # Relationships
    user = relationship("User", back_populates="wallet_members")
    wallet = relationship("Wallet", back_populates="members")
