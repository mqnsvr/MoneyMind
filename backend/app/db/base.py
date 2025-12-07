from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


# Wichtig: hier alle Models importieren, damit sie registriert werden
from app.models.user import User 
from app.models.wallet import Wallet
from app.models.wallet_member import WalletMember  
from app.models.budget import Budget  
from app.models.expense import Expense  
from app.models.category import Category  