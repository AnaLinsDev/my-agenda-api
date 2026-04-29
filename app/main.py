import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from app.routes import activity_routes, auth_routes, user_routes
from .database import Base, engine


from fastapi.exceptions import RequestValidationError
from .errors.error_handlers import (
    validation_exception_handler,
    app_error_handler,
    global_exception_handler
)
from .errors.errors import AppError

load_dotenv()

CLIENT_URL = os.getenv("CLIENT_URL")

RUN_MIGRATIONS = os.getenv("RUN_MIGRATIONS", "false").lower() == "true"

is_prod = os.getenv("ENV") == "prod"

app = FastAPI(
    docs_url=None if is_prod else "/docs",
    redoc_url=None if is_prod else "/redoc",
    openapi_tags=[
        {"name": "Auth", "description": "Authentication endpoints"},
        {"name": "Users", "description": "User management"},
        {"name": "Activities", "description": "Activity management"},
    ]
)

if RUN_MIGRATIONS:
    Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(activity_routes.router)

# middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CLIENT_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register handlers
app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
