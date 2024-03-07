from fastapi import FastAPI
from app.api.endpoints import recipes, users

app = FastAPI()

app.include_router(recipes.router, prefix="/api/v1/recipes")
app.include_router(users.router, prefix="/api/v1/users")
