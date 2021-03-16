import typing
from fae import schemas, models
from sqlalchemy.orm import Session


def get_users(db: Session) -> typing.List[schemas.UserInResponse]:
    return db.query(models.User).all()


def get_user(db: Session, **kwargs):
    return db.query(models.User).filter_by(**kwargs)


def create_user(db: Session, user: schemas.UserInRequest):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    deleted_user = get_user(db=db, id=user_id)
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return deleted_user


def edit_user(db: Session, user_id: int, user: schemas.UserInRequestEdit):
    db.query(models.User).filter(models.User.id == user_id).update(user.dict(exclude_none=True))
    db.commit()
    return get_user(db=db, id=user_id)
