import redis.asyncio as aioredis
from app.config import settings

redis: aioredis.Redis | None = None


async def create_redis():
    global redis
    redis = aioredis.from_url(settings.redis_url, decode_responses=True)


async def close_redis():
    global redis
    if redis:
        await redis.close()


def get_redis() -> aioredis.Redis:
    assert redis is not None, "Redis not initialized"
    return redis
