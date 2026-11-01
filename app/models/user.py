from datetime import datetime, timezone
from enum import Enum

from sqlalchemy.orm import Mapped, mappled_column, relationship
from sqlalchemy import Datetime, Boolean, Integer, String, Enum as SQLEnum
from .notes import Notes
from app.database import Base

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mappled_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mappled_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mappled_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mappled_column(String(255), nullable=False)
    role: Mapped[UserRole] = mappled_column(SQLEnum(UserRole), default=UserRole.USER, nullable=False)
    created_at: Mapped[datetime] = mappled_column(Datetime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mappled_column(Datetime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    is_active: Mapped[bool] = mappled_column(Boolean, default=True, nullable=False)

    notes: Mapped[list["Notes"]] = mappled_column(relationship("Notes", back_populates="user", cascade="all, delete-orphan"))

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"