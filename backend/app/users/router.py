from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.users import service
from app.users.schemas import UserCreate, UserResponse, UserUpdate, UserWithToken

router = APIRouter()


@router.post("", response_model=UserWithToken, status_code=201)
async def create_user(data: UserCreate):
    return await service.create_user(data.name)


@router.get("/{user_id}/token")
async def get_token(user_id: int):
    token = await service.get_token(user_id)
    return {"token": token}


@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    data: UserUpdate,
    current_user_id: int = Depends(get_current_user),
):
    return await service.update_user(user_id, data.name, current_user_id)


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    current_user_id: int = Depends(get_current_user),
):
    await service.delete_user(user_id, current_user_id)
