from pydantic import BaseModel


# Define a Pydantic model for the payload
class SignUpSchema(BaseModel):
    username: str
    password: str
    

class LoginSchema(BaseModel):
    username: str
    password: str