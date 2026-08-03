# Dynamic Route
# Query Parameter

from fastapi import APIRouter

router = APIRouter()


# Single Query Parameter
@router.get("/username")
def get_user(name:str = None): # name (parameter), str (type), None (default value)
    return {
        "Username" : f"You will win, {name}"
    }

@router.get("/age")
def get_user(age:int = 18): # name (parameter), str (type), None (default value)
    if age<18:
        return {
            "Username" : f"You can not vote, {age}"
        }
    return {
        "Username" : f"You can vote, {age}"
        }

# Multiple Query Parameter
@router.get("/laptop")
def get_laptop(brand:str=None, ram:int=8):
    return {
        "message":f"Your {brand} laptop has {ram}GB RAM"
    }
# /laptop?brand=lenovo&ram=32