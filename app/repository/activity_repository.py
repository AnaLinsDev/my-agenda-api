from sqlalchemy.orm import Session
from app.models.activity import Activity

def get_all(db: Session):
    return db.query(Activity).all()

def get_by_date_range(
    db,
    start_date: str,
    end_date: str,
    user_id: str,
    category: str | None = None,
    completed: bool | None = None,
):
    query = db.query(Activity).filter(
        Activity.user_id == user_id,
        Activity.date >= start_date,
        Activity.date <= end_date,
    )

    if category:
        query = query.filter(Activity.category == category)

    if completed is not None:
        query = query.filter(Activity.completed == completed)

    query = query.order_by(Activity.date, Activity.time)

    return query.all()

def create(db: Session, activity: Activity):
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

def update(db: Session, activity_id: str, activity_data, user_id: str):
    activity = db.query(Activity).filter(Activity.user_id == user_id).filter(Activity.id == activity_id).first()

    if not activity:
        return None

    activity.title = activity_data.title
    activity.date = activity_data.date
    activity.time = activity_data.time
    activity.category = activity_data.category
    activity.completed = activity_data.completed

    db.commit()
    db.refresh(activity)

    return activity

def delete(db: Session, activity_id: str, user_id: str):
    activity = db.query(Activity).filter(Activity.user_id == user_id).filter(Activity.id == activity_id).first()

    if activity:
        db.delete(activity)
        db.commit()

    return activity