from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

router = APIRouter(
    prefix="/request_body_validation",
    tags=["request_body_validation"]
)


class Blog(BaseModel):
    id: int
    title: str
    abstract: str

    model_config = ConfigDict(extra="forbid")


@router.post("/post_blog")
def post_blog(data: Blog):
    return {
        "status_code": 200,
        "data": data
    }
