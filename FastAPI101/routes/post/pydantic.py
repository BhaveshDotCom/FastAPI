from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
# Pydantic is a Python library used for data validation, parsing, and serialization

router = APIRouter()

# Validation --> pydantic
class User(BaseModel):
    model_config = ConfigDict(extra="allow")
    name:str
    age:int
    company:str
    role:str

'''
import ConfigDict
By default, Pydantic only validates and stores the fields that are explicitly defined in the model. If the incoming JSON contains additional fields that are not part of the model, those fields are ignored.

Pydantic provides three options to control this behavior using the extra configuration:

extra="ignore" (Default)
Extra fields are accepted in the request but are ignored and not included in the model.

extra="forbid"
Any extra field not defined in the model causes a validation error, and the request is rejected.

extra="allow"
Extra fields are accepted, validated as generic data, and stored in the model along with the defined fields.
'''
@router.post("/portfolio")
def create_profile(data:User): # validation ??
    return {
        "message" : "Account Created",
        "data" : data
    }

# Nested 

class Person(BaseModel):
    name:str=None
    company:str=None
    address:Address

class Address(BaseModel):
    house_no:str=None
    street_no:int=None
    state:str=None
    country:str="India"

@router.post("/account")
def create_account(data:Person):
    return {
        "message" : "Account Created",
        "data" : data
    }