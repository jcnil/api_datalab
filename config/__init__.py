from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import urls, db

version = 1

app = FastAPI(
    title="DATA LAB",
    description="API for management cars",
    version=f"v{version}",
    redoc_url=f"/api/v{version}/redoc",
    docs_url=f"/api/v{version}/docs"
)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    urls.urls
)

app.add_event_handler(
    "startup",
    db.connect_db
)
