from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class NoteBase(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=1000)

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: str | None = Field(None, max_length=100)
    content: str | None = Field(None, max_length=1000)

class NoteResponse(NoteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    