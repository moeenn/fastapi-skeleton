from pydantic import BaseModel, EmailStr, Field
from dataclasses import dataclass


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


@dataclass
class LoginResponse:
    token: str
