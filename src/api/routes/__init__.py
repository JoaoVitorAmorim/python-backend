from fastapi import APIRouter
from src.api.routes.ong import router as ong_router

router = APIRouter()

router.include_router(ong_router, prefix="/ong", tags=["Ongs"])