from datetime import datetime
from pydantic import EmailStr,BaseModel



class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class UserCreateResponse(BaseModel):
    name: str
    created_at: datetime
    id: str
    
    