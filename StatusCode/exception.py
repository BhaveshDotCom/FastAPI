from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
app = FastAPI()

# custom exception and global handling

# custom exception
class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

# gloab exception handler
@app.exception_handler(UserNotFoundException)
def user_not_found(request:Request, exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"{exc.name} not found"

        }
    )

@app.get("/user/{username}")
def get_user(name:str):
    if name!="Bhavesh Upadhyay":
        raise UserNotFoundException(name)
    return {
        "message" : "You Won"
    }