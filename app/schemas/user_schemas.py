from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from app.models.user import UserRole, User
from app.schemas.notes_schemas import NoteResponse 

class UserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr
    role: UserRole = UserRole.USER
    is_active: bool = True

class UserRegister(UserBase):
    password: str = Field(..., max_length=255)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=255)

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    notes: list[NoteResponse] = []  