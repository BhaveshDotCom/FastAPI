from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict

router = APIRouter(
    prefix="/response_models",
    tags=["response_models"]
)

# We can control response structure using pydantic


class BlogIn(BaseModel):
    id: int = 0
    title: str = None
    abstract: str = None
    model_config = ConfigDict(extra="forbid")


class BlogOut(BaseModel):
    platform: str
    blog: BlogIn


'''
@router.post("/post_blog", response_model=BlogOut)
def post_blog(blog: BlogIn) -> BlogOut:
    return {
        "platform": "Medium",
        "blog": blog
    }
'''


@router.post("/post_blog", response_model=list[BlogOut])
def post_blog(blog: BlogIn) -> list[BlogOut]:
    return [{
        "platform": "Medium",
        "blog": blog
    }]
