import typing
from fae.api.v1.app import dependencies
from sqlalchemy.orm import Session
from fae import schemas, crud
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()


@router.get("/users", response_model=typing.List[schemas.UserInResponse])
async def get_users(db: Session = Depends(dependencies.get_db)):
    return crud.get_users(db=db)


@router.get("/users/{user_id}", response_model=schemas.UserInResponse)
async def get_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    user = crud.get_user(db=db, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=schemas.UserInResponse)
async def create_user(user: schemas.UserInRequest, db: Session = Depends(dependencies.get_db)):
    if crud.get_user(db=db, email=user.email) is not None:
        raise HTTPException(status_code=400, detail="USer is already exists")

    return crud.create_user(db=db, user=user)


@router.patch("/users/{user_id}", response_model=schemas.UserInResponse)
async def edit_user(
        user_id: int,
        user: schemas.UserInRequestEdit,
        db: Session = Depends(dependencies.get_db)
):
    new_data = user.dict(exclude_none=True)
    if new_data == {}:
        raise HTTPException(status_code=400, detail="Provide a new data")

    return crud.edit_user(
        db=db,
        user_id=user_id,
        user=schemas.UserInRequestEdit(**new_data)
    )


@router.delete("/users/{user_id}", response_model=schemas.UserInResponse)
async def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_user(db=db, user_id=user_id)