from fastapi import FastAPI, Response, Request
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
import json

app = FastAPI()


@app.middleware("http")
async def request_details(request: Request, call_next):
    print(request["path"])
    print(request["method"])
    payload = await request.body()
    if payload:
        print(json.loads(payload))
    response = await call_next(request)
    return response

# local variable for todos
db: list[Todo] = []


# pydantic model for todos
class Todo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    priority: str
    is_done: bool = False


class BaseOut(BaseModel):
    msg: str
    error: str = None


class TodoCreateOut(BaseOut):
    todo: Todo


# APIs
@app.post("/create", response_model=TodoCreateOut)
def create_todo(todo: Todo) -> TodoCreateOut:
    db.append(todo)
    return TodoCreateOut(
        todo=todo,
        msg="Todo Created Successfully"
    )


class TodoGetOut(BaseOut):
    todos: list[Todo]


@app.get("/todos")
def get_todos():
    return Response(
        content=TodoGetOut(
            todos=db,
            msg="All Todos Fetched Successfully"
        ).model_dump_json(),
        status_code=200,
    )


@app.get("/todo/{id}", response_model=TodoCreateOut | BaseOut)
def get_todo(id: str) -> TodoCreateOut | BaseOut:
    try:
        id = UUID(id)
    except Exception as e:
        return BaseOut(
            msg="Wrong Todo ID",
            error=str(e)
        )

    for todo in db:
        if todo.id == id:
            return TodoCreateOut(
                todo=todo,
                msg="Todo Fetched Successfully"
            )
    return BaseOut(
        msg="Todo Not Found"
    )


@app.delete("/delete_todo/{id}", response_model=BaseOut)
def delete_todo(id: str) -> BaseOut:
    try:
        id = UUID(id)
    except Exception as e:
        return BaseOut(
            msg="Wrong Todo ID",
            error=str(e)
        )

    for i, todo in enumerate(db):
        if todo.id == id:
            del db[i]
    return BaseOut(
        msg="Todo Deleted Successfully"
    )


# Fetch Todo by Priority
@app.get("/todo")
def get_todo_by_priority(priority: str):
    todos: list[Todo] = []

    for todo in db:
        if todo.priority == priority:
            todos.append(todo)

    if not todos:
        return BaseOut(
            msg=f"No {priority} Priority task available"
        )

    return TodoGetOut(
        todos=todos,
        msg=f"All {priority} priority tasks fetched successfully"
    )
