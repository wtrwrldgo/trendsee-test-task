import asyncpg

from app.database import get_pool


async def create_user(name: str) -> asyncpg.Record:
    pool = get_pool()
    return await pool.fetchrow(
        "INSERT INTO users (name) VALUES ($1) RETURNING id, name, created_at",
        name,
    )


async def get_user_by_id(user_id: int) -> asyncpg.Record | None:
    pool = get_pool()
    return await pool.fetchrow(
        "SELECT id, name, created_at FROM users WHERE id = $1",
        user_id,
    )


async def update_user(user_id: int, name: str) -> asyncpg.Record | None:
    pool = get_pool()
    return await pool.fetchrow(
        "UPDATE users SET name = $1 WHERE id = $2 RETURNING id, name, created_at",
        name,
        user_id,
    )


async def delete_user(user_id: int) -> bool:
    pool = get_pool()
    result = await pool.execute("DELETE FROM users WHERE id = $1", user_id)
    return result == "DELETE 1"
