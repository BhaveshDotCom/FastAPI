from fastapi import APIRouter

router = APIRouter()

@router.post("/profile")
def create_profile(name:str=None, code:int=None):
    return {
        "message" : f"Hey {name}, Your code is {code}"
    }

# Use Case
@router.post("/profile_card")
def create_profile(data:dict): # validation ??
    return {
        "message" : "Account Created",
        "data" : data
    }