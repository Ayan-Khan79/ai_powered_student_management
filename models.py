from pydantic import BaseModel, EmailStr
from typing import Optional
# pydantic used for automatic validation of input request data

class Student(BaseModel):
    name: str
    age: int # 23.8 = 23
    course: str
    email: Optional[EmailStr] = None

class Professor(BaseModel):
    pid : int
    name: str
    experience : int
    subject : str
    email : Optional[EmailStr]  = None

class Feedback(BaseModel):
    text:str
