from pydantic import BaseModel, Field, ValidationError
from pydantic import field_validator
from typing import Optional

class User(BaseModel):
    username: str
    #username: str = Field(min_length=4, max_length=50)
    password: str
    email: str
    age: Optional[int] = None

    @field_validator('username')
    def username_validator(cls, username):
        if len(username) < 4:
            raise ValueError("La longitud mínima es de cuatro (4) caracteres.")
        if len(username) > 50:
            raise ValueError("La longitud máxima es de cincuenta (50) caracteres.")
        return username
    
try:
    user = User( username="ola", password="12345", email="abnersaavedra@gmail.com", age=33)
    #print("User: ", user)
except ValidationError as e:
    print(e.json())