from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user_id
from app.schemas.activity_schema import Activity, ActivityBase, ActivityCreate
from app.services import activity_service

router = APIRouter(prefix="/activities", tags=["Activities"])

# Activity List
@router.get("/", response_model=list[Activity])
def get_all(
    week_start: str = Query(..., description="YYYY-MM-DD"),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    start_date = datetime.strptime(week_start, "%Y-%m-%d")
    end_date = start_date + timedelta(days=6)

    return activity_service.get_activities_by_week(
        db,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
        user_id
    )

# Create new Activity
@router.post("/", response_model=Activity)
def create(
    activity: ActivityCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    return activity_service.add_activity(db, activity, user_id)

# Update the Activity
@router.put("/{id}", response_model=Activity)
def update(
    id: str,
    activity: ActivityBase,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    return activity_service.update_activity(db, id, activity, user_id)

# Delete the Activity
@router.delete("/{id}")
def delete(
    id: str,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id)
):
    activity_service.delete_activity(db, id, user_id)

    return {"message": "Deleted successfully"}