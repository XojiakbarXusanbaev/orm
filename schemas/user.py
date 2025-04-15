from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    username: str

    class Config:
        from_attributes = True
