import os
from fastapi import FastAPI
from dotenv import load_dotenv

from .database import Base, engine
from .routes import router

from fastapi.exceptions import RequestValidationError
from .error_handlers import (
    validation_exception_handler,
    app_error_handler,
    global_exception_handler
)
from .errors import AppError

load_dotenv()

RUN_MIGRATIONS = os.getenv("RUN_MIGRATIONS", "false").lower() == "true"

app = FastAPI()

if RUN_MIGRATIONS:
    Base.metadata.create_all(bind=engine)

app.include_router(router)

# register handlers
app.add_exception_handler(AppError, app_error_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)