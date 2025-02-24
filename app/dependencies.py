from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Header, HTTPException
def get_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid authorization format")
    return authorization.split(" ")[1]



# Ваші налаштування підключення до бази даних
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/lucidt"

# Створення SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})

# Створення сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функція для отримання сесії бази даних
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
