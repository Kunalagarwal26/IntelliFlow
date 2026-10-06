from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "IntelliFlow",
        "status": "running",
    }


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }