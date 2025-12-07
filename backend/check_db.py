from app.db.session import engine
from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(text("SELECT tablename FROM pg_tables WHERE schemaname='public';"))
    print(result.fetchall())