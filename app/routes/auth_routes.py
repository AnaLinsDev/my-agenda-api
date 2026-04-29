from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from ..services.auth_service import login_user, register_user
from ..schemas.auth_schema import AuthResponse, LoginRequest, RegisterRequest
from ..database import get_db

from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv("ENV")

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# Auth Register
@router.post("/register", response_model=AuthResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, data)


# Auth Login
@router.post("/login", response_model=AuthResponse)
def login(
    data: LoginRequest,
    response: Response,
    db: Session = Depends(get_db),
):
    return login_user(db, response, data)


# Auth Logout
@router.post("/logout")
def logout(response: Response):
    response.set_cookie(
        key="access_token",
        value="",
        max_age=0,
        expires=0,
        httponly=True,
        secure=ENV == "prod",
        samesite="none" if ENV == "prod" else "lax",
        path="/",
    )
    return {"message": "Logged out successfully"}