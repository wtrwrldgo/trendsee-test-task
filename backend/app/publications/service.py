import asyncio
import json

from fastapi import HTTPException, status

from app.publications import repository
from app.publications.schemas import PaginatedPublications, PublicationResponse
from app.redis_client import get_redis

CACHE_TTL = 600  # 10 minutes


def _record_to_response(row) -> PublicationResponse:
    return PublicationResponse(
        id=row["id"],
        user_id=row["user_id"],
        title=row["title"],
        content=row["content"],
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )


async def create_publication(user_id: int, title: str, content: str) -> PublicationResponse:
    row = await repository.create_publication(user_id, title, content)
    pub = _record_to_response(row)

    # Cache in Redis
    r = get_redis()
    await r.setex(f"pub:{pub.id}", CACHE_TTL, pub.model_dump_json())

    # Invalidate user publications list cache
    await r.delete(f"user_pubs:{user_id}")

    return pub


async def get_user_publications(
    user_id: int, limit: int, offset: int
) -> PaginatedPublications:
    r = get_redis()
    cache_key = f"user_pubs:{user_id}:{limit}:{offset}"

    # Check Redis cache
    cached = await r.get(cache_key)
    if cached:
        return PaginatedPublications.model_validate_json(cached)

    # Simulate slow DB read
    await asyncio.sleep(2)

    rows = await repository.get_publications_by_user(user_id, limit, offset)
    total = await repository.count_publications_by_user(user_id)
    items = [_record_to_response(row) for row in rows]

    result = PaginatedPublications(items=items, total=total, limit=limit, offset=offset)

    # Cache result
    await r.setex(cache_key, CACHE_TTL, result.model_dump_json())

    return result


async def update_publication(
    pub_id: int, title: str | None, content: str | None, current_user_id: int
) -> PublicationResponse:
    existing = await repository.get_publication_by_id(pub_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")
    if existing["user_id"] != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")

    row = await repository.update_publication(pub_id, title, content)
    pub = _record_to_response(row)

    # Update cache
    r = get_redis()
    await r.setex(f"pub:{pub.id}", CACHE_TTL, pub.model_dump_json())
    await r.delete(f"user_pubs:{pub.user_id}")

    return pub


async def delete_publication(pub_id: int, current_user_id: int) -> None:
    existing = await repository.get_publication_by_id(pub_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publication not found")
    if existing["user_id"] != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed")

    await repository.delete_publication(pub_id)

    # Invalidate caches
    r = get_redis()
    await r.delete(f"pub:{pub_id}")
    await r.delete(f"user_pubs:{existing['user_id']}")
