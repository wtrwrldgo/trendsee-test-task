import asyncpg

from app.database import get_pool


async def create_publication(user_id: int, title: str, text: str) -> asyncpg.Record:
    pool = get_pool()
    return await pool.fetchrow(
        """INSERT INTO publications (user_id, title, "text")
           VALUES ($1, $2, $3)
           RETURNING id, user_id, title, "text", created_at, updated_at""",
        user_id,
        title,
        text,
    )


async def get_publication_by_id(pub_id: int) -> asyncpg.Record | None:
    pool = get_pool()
    return await pool.fetchrow(
        'SELECT id, user_id, title, "text", created_at, updated_at FROM publications WHERE id = $1',
        pub_id,
    )


async def get_publications_by_user(user_id: int, limit: int, offset: int) -> list[asyncpg.Record]:
    pool = get_pool()
    return await pool.fetch(
        """SELECT id, user_id, title, "text", created_at, updated_at
           FROM publications WHERE user_id = $1
           ORDER BY created_at DESC LIMIT $2 OFFSET $3""",
        user_id,
        limit,
        offset,
    )


async def count_publications_by_user(user_id: int) -> int:
    pool = get_pool()
    row = await pool.fetchrow(
        "SELECT COUNT(*) as cnt FROM publications WHERE user_id = $1",
        user_id,
    )
    return row["cnt"]


async def update_publication(pub_id: int, title: str | None, text: str | None) -> asyncpg.Record | None:
    pool = get_pool()
    current = await get_publication_by_id(pub_id)
    if not current:
        return None
    new_title = title if title is not None else current["title"]
    new_text = text if text is not None else current["text"]
    return await pool.fetchrow(
        """UPDATE publications SET title = $1, "text" = $2, updated_at = NOW()
           WHERE id = $3
           RETURNING id, user_id, title, "text", created_at, updated_at""",
        new_title,
        new_text,
        pub_id,
    )


async def delete_publication(pub_id: int) -> bool:
    pool = get_pool()
    result = await pool.execute("DELETE FROM publications WHERE id = $1", pub_id)
    return result == "DELETE 1"
