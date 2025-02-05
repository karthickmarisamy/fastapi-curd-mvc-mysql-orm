from pydantic import BaseModel
from typing import Optional

class CustomerSchema(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    age: Optional[str] = None
        
    class config:
        orm_mode= True