from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_schema import UpdateUserRequest, UserResponse
from app.dependencies.auth import get_current_user
from app.services.user_service import update_user, delete_user

from dotenv import load_dotenv
import os

load_dotenv()

ENV = os.getenv("ENV")

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Get Profile
@router.get("/profile", response_model=UserResponse)
def get_profile(current_user=Depends(get_current_user)):
    return current_user


# Update User
@router.put("/edit", response_model=UserResponse)
def update(
    data: UpdateUserRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_user(current_user, db, data)


# Delete User
@router.delete("/delete")
def delete(
    response: Response,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    delete_user(current_user, db)

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

    return {"message": "User deleted successfully"}