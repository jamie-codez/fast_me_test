from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: constr(min_length=8, max_length=128)
    password_confirm: constr(min_length=8, max_length=128)
    role: str = "user"
    verified: bool = False
    is_active: bool = True
    is_superuser: bool = False


class LoginUserSchema(BaseModel):
    username: str
    password: constr(min_length=8, max_length=128)


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
