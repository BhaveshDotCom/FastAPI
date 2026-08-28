from fastapi import FastAPI
from app.routers import apis, routes, request_body_validation
from app.routers import response_models, return_pydantic_model

app = FastAPI(
    title="FastAPI Learning Docs",
    description="FastAPI is a fast and modern Python framework for building "
    "reliable, scalable REST APIs with automatic documentation and data "
    "validation.",
    version="0.0.1"
)

app.include_router(apis.router)
app.include_router(routes.router)
app.include_router(request_body_validation.router)
app.include_router(response_models.router)
app.include_router(return_pydantic_model.router)
