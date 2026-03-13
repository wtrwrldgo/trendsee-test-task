from datetime import datetime

from pydantic import BaseModel


class PublicationCreate(BaseModel):
    title: str
    content: str


class PublicationUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PublicationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


class PaginatedPublications(BaseModel):
    items: list[PublicationResponse]
    total: int
    limit: int
    offset: int
