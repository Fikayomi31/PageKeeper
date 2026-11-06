from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from app.models.user import UserRole
from app.schemas.notes_schemas import NoteResponse 



class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=12)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=255)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    notes: list[NoteResponse] = []  


# Authentication Schemas
 class TokenResponse(BaseModel):
     access_token: str
     token_type: str = "bearer"
     