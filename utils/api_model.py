from pydantic import BaseModel

class AccountInfo(BaseModel):
    id : int
    fullname: str
    username: str
    password: str
    phone: str
    email: str