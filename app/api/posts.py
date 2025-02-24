from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, dependencies
from ..services.auth import verify_token

router = APIRouter()

@router.post("/add_post")
def add_post(post: schemas.PostCreate, token: str = Depends(dependencies.get_token), db: Session = Depends(dependencies.get_db)):
    user_data = verify_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    user_id = user_data.get("sub")
    db_post = crud.create_post(db=db, post=post, user_id=user_id)
    return {"post_id": db_post.id}


@router.get("/posts")
def get_posts(token: str = Depends(dependencies.get_token), db: Session = Depends(dependencies.get_db)):
    user_data = verify_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    user_id = user_data.get("sub")
    posts = crud.get_posts(db=db, user_id=user_id)
    return posts

@router.delete("/delete_post/{post_id}")
def delete_post(post_id: int, token: str = Depends(dependencies.get_token), db: Session = Depends(dependencies.get_db)):
    user_data = verify_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    crud.delete_post(db=db, post_id=post_id)
    return {"message": "Post deleted successfully"}
