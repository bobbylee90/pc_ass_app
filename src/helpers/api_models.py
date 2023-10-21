from pydantic import BaseModel

class Info(BaseModel):
    fullname: str
    email: str
    phone: str
    biography: str
    
class Account(BaseModel):
    username: str
    password: str
    info: Info


