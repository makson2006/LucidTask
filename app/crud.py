from sqlalchemy.orm import Session
from .models import User, Post
from .schemas import UserCreate, PostCreate


# Створення користувача
def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Отримання користувача за email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Створення поста
def create_post(db: Session, post: PostCreate, user_id: str):
    db_post = Post(text=post.text, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
