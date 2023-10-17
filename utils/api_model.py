from pydantic import BaseModel

class AccountInfo(BaseModel):
    id : int
    name: str
    username: str
    password: str
    phone: str
    email: str