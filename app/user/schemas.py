from pydantic import EmailStr, BaseModel

class SUserRegister(BaseModel):
    email: EmailStr
    password: str