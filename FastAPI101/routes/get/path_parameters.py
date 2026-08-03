# Dynamic Route
# Path Parameter

from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id:int):
    return {
        "User ID" : user_id
    }