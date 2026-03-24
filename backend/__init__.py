"""Backend part of the app. Consists entire business logic."""

from fastapi import APIRouter

from backend.src.house.endpoint import router as books_router

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://0.0.0.0:8000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
headers = [
    "Content-Type",
    "Set-Cookie",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
    "Authorization",
]

main_router = APIRouter()
main_router.include_router(books_router)
