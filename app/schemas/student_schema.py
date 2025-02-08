from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentSchema(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[str] = None
        
    class config:
        orm_mode= True