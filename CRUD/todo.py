from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

todos = []

class User(BaseModel):
    id:int=None
    task:str=None
    status:str=None

# Create
@router.post("/add")
def create_todo(data:User):
    todos.append(data)
    return {
        "message" : "Todo Added",
        "data" : data
    }

# Read
@router.get("/todos")
def get_todos():
    return todos

@router.get("/todos/{id}")
def get_todo(id:int):
    for todo in todos:
        if(id == todo.id):
            return todo
    return "task not found"

# Put (Update)
@router.put("/update/{id}")
def update_todo(id:int, updated_todo:User):
    for index, task in enumerate(todos):
        if task.id == id :
            todos[index] = updated_todo
            return {
                "message" : "Task Updated",
                "data" : updated_todo
            }
    return "Error 404" 

# Delete
@router.delete("/delete/{id}")
def delete_todo(id:int):
    for index, task in enumerate(todos):
        if task.id == id :
            todos.pop(index)
            return {
                "message" : "Task Deleted",
            }
    return "Error 404" 
