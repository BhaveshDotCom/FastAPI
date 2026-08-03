from fastapi import FastAPI
from CRUD.todo import router as todo_route

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "app is running"
    }

app.include_router(todo_route)