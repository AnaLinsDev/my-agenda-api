from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from ..services.auth_services import login_user, register_user
from ..schemas.auth_schemas import AuthResponse, LoginRequest, RegisterRequest
from ..database import get_db

router = APIRouter(prefix="/auth")


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
    response.delete_cookie("access_token")
    return {"message": "Logged out successfully"}