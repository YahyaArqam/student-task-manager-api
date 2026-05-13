from pydantic import BaseModel
from typing import Optional

# ─────────────────────────────
# USER SCHEMAS
# ─────────────────────────────

# What user sends when registering
class UserCreate(BaseModel):
    email: str
    password: str

# What we send back about a user
class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True

# ─────────────────────────────
# TOKEN SCHEMAS
# ─────────────────────────────

# What we send back after login
class Token(BaseModel):
    access_token: str
    token_type: str

# Data stored inside the token
class TokenData(BaseModel):
    email: Optional[str] = None

# ─────────────────────────────
# TASK SCHEMAS
# ─────────────────────────────

# What user sends when creating a task
class TaskCreate(BaseModel):
    title: str
    description: str

# What user sends when updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# What we send back about a task
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    owner_id: int

    class Config:
        from_attributes = True