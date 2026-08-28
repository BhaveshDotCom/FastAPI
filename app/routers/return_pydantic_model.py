from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

router = APIRouter(
    prefix="/return_pydantic_model",
    tags=["return_pydantic_model"]
)


class BlogIn(BaseModel):
    id: int
    title: str
    abstract: str
    model_config = ConfigDict(extra="forbid")


class BlogOut(BaseModel):
    platform: str
    blog: BlogIn


@router.post("/post_blog", response_model=BlogOut)
def post_blog(blog: BlogIn) -> BlogOut:
    return BlogOut(platform="Medium", blog=blog)
