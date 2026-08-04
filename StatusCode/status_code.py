from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

# implementing status code
@app.post("/create",status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message" : "User Created"
    }

# implementing HTTPException
@app.get("/top_10_coders/{rank}")
def get_top_10_coders(rank:int):
    if(rank > 10):
        raise HTTPException (
            status_code=404,
            detail="Your are not on the list",
        )
    return {
        "rank":rank,
        "prize":"Free Claude Subscription"
    }