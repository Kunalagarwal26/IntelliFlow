from fastapi import FastAPI

from app.api.v1.router import router


app = FastAPI(
    title="IntelliFlow API",
    description="Enterprise AI Knowledge & Automation Platform",
    version="0.1.0",
)

app.include_router(router)