from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

_users = []

class User(BaseModel):
    name:str=None
    age:int=None

# POST
@app.post("/add_user")
def create_user(user:User):
    _users.append(user)
    return {
        "message" : "User Created",
        "data" : user
    }

# PUT (UPDATE)
@app.put("/update_user/{id}")
def update(id:int, data:User, notify:bool=False):
    if id < len(_users):
        _users[id] = data
        return {
            "message" : "Success",
            "notify" : notify,
            "data" : data
        }
    return {
        "error" : "User 404"
    }