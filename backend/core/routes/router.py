from fastapi import APIRouter

from core.routes import empresa

router = APIRouter()

router.include_router(empresa.router)