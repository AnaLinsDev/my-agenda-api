from sqlalchemy.orm import Session
from app.models.activity import Activity
from app.repository import activity_repository
from app.errors.errors import AppError, ErrorCode

def get_activities_by_week(db, start_date: str, end_date: str, user_id: str):
    return activity_repository.get_by_date_range(db, start_date, end_date, user_id)

def add_activity(db: Session, activity_data, user_id: str):
    activity = Activity(**activity_data.dict())
    activity.user_id = user_id
    return activity_repository.create(db, activity)

def update_activity(db: Session, activity_id: str, activity_data, user_id: str):
    activity = Activity(**activity_data.dict())
    updated = activity_repository.update(db, activity_id, activity, user_id)

    if not updated:
        raise AppError(ErrorCode.ACTIVITY_NOT_FOUND)

    return updated 

def delete_activity(db: Session, activity_id: str, user_id: str):
    deleted = activity_repository.delete(db, activity_id, user_id)

    if not deleted:
        raise AppError(ErrorCode.ACTIVITY_NOT_FOUND)
    
    return "success"