from fastapi import FastAPI

app = FastAPI(
    title="IntelliFlow API",
    description="Enterprise AI Knowledge & Automation Platform",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "IntelliFlow",
        "status": "running",
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }