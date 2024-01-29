from pydantic import BaseModel

class RegistrationData(BaseModel):
    username: str
    password: str
    