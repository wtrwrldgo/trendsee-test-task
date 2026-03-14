from fastapi import APIRouter, Depends, Query

from app.auth.dependencies import get_current_user
from app.publications import service
from app.publications.schemas import (
    PaginatedPublications,
    PublicationCreate,
    PublicationResponse,
    PublicationUpdate,
)

router = APIRouter()


@router.post("", response_model=PublicationResponse, status_code=201)
async def create_publication(
    data: PublicationCreate,
    current_user_id: int = Depends(get_current_user),
):
    return await service.create_publication(current_user_id, data.title, data.text)


@router.get("/user/{user_id}", response_model=PaginatedPublications)
async def get_user_publications(
    user_id: int,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return await service.get_user_publications(user_id, limit, offset)


@router.patch("/{pub_id}", response_model=PublicationResponse)
async def update_publication(
    pub_id: int,
    data: PublicationUpdate,
    current_user_id: int = Depends(get_current_user),
):
    return await service.update_publication(pub_id, data.title, data.text, current_user_id)


@router.delete("/{pub_id}", status_code=204)
async def delete_publication(
    pub_id: int,
    current_user_id: int = Depends(get_current_user),
):
    await service.delete_publication(pub_id, current_user_id)
