# Backend Rules

## Architecture
- Use raw asyncpg queries in `repository.py` — no ORM
- Business logic in `service.py`, HTTP handling in `router.py`
- Pydantic v2 schemas for all request/response models
- FastAPI dependency injection for auth (`get_current_user`)

## Database
- Always use parameterized queries (`$1, $2`) — never string interpolation
- Return `asyncpg.Record` from repositories, convert to Pydantic in services
- Use `RETURNING` clause on INSERT/UPDATE

## Caching
- Redis cache on create with TTL 600s
- Invalidate related cache keys on any mutation (create/update/delete)
- Simulate 2s delay on cache miss for demo purposes

## Security
- JWT tokens expire in 24h
- Users can only modify their own resources (check `user_id` match)
- CORS allows all origins (dev mode) — restrict in production
