from fastapi import FastAPI
from .api import users, posts

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
