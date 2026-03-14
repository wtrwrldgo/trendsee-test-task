# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

Trendsee test task — fullstack publication feed service.
- **Backend**: FastAPI + PostgreSQL + Redis + JWT (`/backend`)
- **Frontend**: Vue 3 + TypeScript + Vite (`/frontend`)
- **Infrastructure**: Docker Compose with 4 services

## Project Structure

```
backend/app/
├── main.py              # FastAPI app, CORS, lifespan
├── config.py            # Settings (DB, Redis, JWT)
├── database.py          # asyncpg connection pool
├── redis_client.py      # aioredis connection
├── auth/                # JWT create/decode, get_current_user DI
├── users/               # CRUD: router, service, repository, schemas
└── publications/        # CRUD with Redis caching: router, service, repository, schemas

frontend/src/
├── api/index.ts         # Axios client with JWT interceptor
├── views/               # FeedView, Page1 (video grid), Page2 (analysis)
├── components/          # PostCard, PostModal, LoadingSpinner
├── composables/         # useInfiniteScroll
└── router/              # Vue Router config
```

## Key Patterns

### Backend
- Raw asyncpg queries (no ORM) — all in `repository.py` files
- Pydantic v2 for request/response validation
- Service layer handles business logic + Redis caching
- Cache TTL: 600s. Cache miss adds `asyncio.sleep(2)` simulated delay
- JWT auth via `get_current_user` FastAPI dependency
- Redis key patterns: `pub:{id}`, `user_pubs:{user_id}:{limit}:{offset}`
- Cache invalidation uses SCAN-based pattern delete for `user_pubs:{user_id}:*`

### Frontend
- Vue 3 Composition API with `<script setup lang="ts">`
- Scoped styles per component
- Axios interceptor auto-attaches Bearer token from localStorage
- Infinite scroll via `useInfiniteScroll` composable (500px threshold)

## Commands

```bash
# Start everything
docker-compose up --build

# Frontend dev (standalone)
cd frontend && npm run dev

# Backend dev (standalone)
cd backend && uvicorn app.main:app --reload
```

## API Endpoints

- `POST /users` — create user (returns JWT)
- `GET /users/{id}/token` — get JWT
- `PATCH /users/{id}` — update (auth)
- `DELETE /users/{id}` — delete (auth)
- `POST /publications` — create (auth)
- `GET /publications/user/{id}?limit=10&offset=0` — paginated list
- `PATCH /publications/{id}` — update (auth)
- `DELETE /publications/{id}` — delete (auth)

## Rules

- Keep backend responses consistent with Pydantic schemas
- Always invalidate Redis cache on mutations
- Frontend: use scoped styles, Composition API, TypeScript
- Never commit `.env` or secrets
