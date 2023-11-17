from fastapi import APIRouter
from src.api.autocomplete import autocomplete_router
from src.api.auth import router as auth_router
from src.api.tags import router as tag_router
from src.api.rating import router as rating_router

router = APIRouter(prefix='/v1')

router.include_router(rating_router)
router.include_router(autocomplete_router)
router.include_router(auth_router)
router.include_router(tag_router)

