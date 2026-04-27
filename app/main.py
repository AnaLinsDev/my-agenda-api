import os
from fastapi import FastAPI
from dotenv import load_dotenv

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

RUN_MIGRATIONS = os.getenv("RUN_MIGRATIONS", "false").lower() == "true"

app = FastAPI(
    openapi_tags=[
        {"name": "Auth", "description": "Authentication endpoints"},
        {"name": "Users", "description": "User management"},
    ]
)

if RUN_MIGRATIONS:
    Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(activity_routes.router)

# register handlers
app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)