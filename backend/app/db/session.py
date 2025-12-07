from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create database engine using connection URL from settings
engine = create_engine(settings.database_url, future=True)


# Session factory: creates new database sessions
# autoflush=False: don't auto-sync changes to DB before queries
# autocommit=False: require explicit commit() for changes
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)

def get_db():
    """
    Dependency that provides a database session.
    Yields a session and ensures it's closed after use.
    Usage: Depends(get_db) in FastAPI route functions.
    """
    db = SessionLocal()
    try:
        yield db  # Provide session to the route
    finally:
        db.close()  # Always close session after request