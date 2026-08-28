from fastapi import APIRouter

# create an route of FastAPI
router = APIRouter(
    prefix="/apis",
    tags=["Apis"]
)


# API
@router.get("/")  # decorator - method(get) - route
def hello():
    return {
        "message": "Hello, Developer!!"
    }


@router.get("/stack")
def role():
    return {
        "language": "Python",
        "database": "MongoDB"
    }
