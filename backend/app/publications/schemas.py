from datetime import datetime

from pydantic import BaseModel


class PublicationCreate(BaseModel):
    title: str
    text: str


class PublicationUpdate(BaseModel):
    title: str | None = None
    text: str | None = None


class PublicationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    text: str
    created_at: datetime
    updated_at: datetime


class PaginatedPublications(BaseModel):
    items: list[PublicationResponse]
    total: int
    limit: int
    offset: int
