from fastapi import APIRouter

router = APIRouter(
    prefix="/routes",
    tags=["routes"]
)


@router.post("/create")
def create(data: dict):
    return {
        "status": 200,
        "data": data
    }


# Path Parameter
@router.put("/update/{id}")
def update(id: str, data: dict):
    return {
        "status": 200,
        "id": id,
        "data": data
    }


# Query Parameter
@router.get("/update")
def get(q: str):
    return {
        "status": 200,
        "q": q
    }


# Delete
@router.delete("delete/{id}")
def delete(id: str):
    return {
        "status": 200,
        "id": id,
    }
