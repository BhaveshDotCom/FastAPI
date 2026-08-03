from fastapi import APIRouter

router = APIRouter()

# About Roue
@router.get("/about")
def about():
    return {
        "Name" : "Bhavesh Upadhyay",
        "Mail" : "bhaveshupadhyay256@gmail.com",
        "Company" : "Google",
        "Role" : "Machine Learning Engineer"
    }