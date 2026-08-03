from fastapi import FastAPI
from FastAPI101.routes.get.about import router as about_route
from FastAPI101.routes.get.path_parameters import router as user_id_route
from FastAPI101.routes.get.query_parameters import router as username_route
from FastAPI101.routes.post.request import router as profile_route
from FastAPI101.routes.post.pydantic import router as account_route
app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {
        f"Hello, This is Bhavesh"
        }

app.include_router(about_route)
app.include_router(user_id_route)
app.include_router(username_route)
app.include_router(profile_route)
app.include_router(account_route)