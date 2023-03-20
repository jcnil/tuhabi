import sentry_sdk
from fastapi import FastAPI,Request
from starlette.responses import JSONResponse

from app.core.constants import SENTRY_DSN, APP_ENV
from config import urls, settings

version = 1

app = FastAPI(
    title="Hydra",
    description="",
    version=f"v{version}",
    docs_url=f"/api/v{version}/docs"
)

"""
Initialize Sentry
"""

sentry_sdk.init(
    dsn=SENTRY_DSN,
    environment=APP_ENV,
    traces_sample_rate=1.0
)

app.include_router(
    urls.urls
)

@app.exception_handler(Exception)
async def internal_server_exception_handler(request: Request, exc: Exception):
    sentry_sdk.capture_exception(exc)
    response: dict = {"messages": "Internal Server Error"}
    return JSONResponse(content=response, status_code=500)

settings.connect_db()
