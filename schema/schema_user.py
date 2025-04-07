from pydantic import BaseModel
from typing import Optional
from fastapi import Form




class Auth(BaseModel):
    username: str
    password: str
    role: str

class Register(Auth):
    role: Optional[str] = 'user'
    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...),
    ):
        return cls(username = username, password = password)

class Login(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...),
    ):
        return cls(username=username, password=password)
    
