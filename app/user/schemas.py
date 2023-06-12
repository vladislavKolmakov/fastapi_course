from pydantic import EmailStr, BaseModel

class SUserAuth(BaseModel):
    email: EmailStr
    password: str