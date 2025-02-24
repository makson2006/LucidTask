from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    email: str
    id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    text: str

class PostOut(BaseModel):
    id: int
    text: str
    user_id: int

    class Config:
        orm_mode = True
