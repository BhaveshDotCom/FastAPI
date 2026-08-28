from fastapi import FastAPI, APIRouter, HTTPException
from config import collection
from database.schemas import all_tasks
from database.models import Todo
from datetime import datetime
from bson import ObjectId

app = FastAPI()
router = APIRouter()


@router.get("/")
async def get_todos():
    data = collection.find()
    return all_tasks(data)


@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {
            "status": 200,
            "id": str(resp.inserted_id)
        }
    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=f"Error: {e}"
            )


@router.post("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id}, {"is_deleted": False})
        if not existing_doc:
            return HTTPException(
                status_code=404,
                detail="Task not found"
            )
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id": id}, {"set": dict(updated_task)})
        return {
                    "status": 200,
                    "resp": resp
                }

    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=f"Error: {e}"
        )


@router.delete("/")
async def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id}, {"is_deleted": False})
        if not existing_doc:
            return HTTPException(
                status_code=404,
                detail="Task not found"
            )
        resp = collection.delete_one({"_id": id})
        return {
                    "status": 200,
                    "deleted_count": str(resp.deleted_count)
                }

    except Exception as e:
        return HTTPException(
            status_code=500,
            detail=f"Error: {e}"
        )

app.include_router(router)
