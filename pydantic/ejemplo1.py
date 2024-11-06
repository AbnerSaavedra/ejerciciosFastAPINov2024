from pydantic import BaseModel
from pydantic import ValidationError
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    email: str
    age: Optional[int] = None


#user = User(username="Abner", password="12345", email="abnersaavedra@gmail.com", age=33)
"""user = User( password="12345", email="abnersaavedra@gmail.com", age=33)

print("User: ", user)"""

# Creemos una instancia user dentro de un bloque try...except

try:
    user = User( password="12345", email="abnersaavedra@gmail.com", age=33)
    #print("User: ", user)
except ValidationError as e:
    print(e.json())
