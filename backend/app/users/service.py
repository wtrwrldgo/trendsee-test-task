from fastapi import HTTPException, status

from app.auth.jwt import create_token
from app.users import repository
from app.users.schemas import UserResponse, UserWithToken


async def create_user(name: str) -> UserWithToken:
    row = await repository.create_user(name)
    user = UserResponse(id=row["id"], name=row["name"], created_at=row["created_at"])
    token = create_token(user.id)
    return UserWithToken(user=user, token=token)


async def get_token(user_id: int) -> str:
    row = await repository.get_user_by_id(user_id)
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return create_token(user_id)


async def update_user(user_id: int, name: str, current_user_id: int) -> UserResponse:
    if user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    row = await repository.update_user(user_id, name)
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse(id=row["id"], name=row["name"], created_at=row["created_at"])


async def delete_user(user_id: int, current_user_id: int) -> None:
    if user_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")
    deleted = await repository.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
