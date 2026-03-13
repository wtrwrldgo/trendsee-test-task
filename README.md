# Trendsee Test Task

Fullstack publication feed service: FastAPI + PostgreSQL + Redis + JWT backend, Vue 3 + TypeScript frontend.

## Quick Start

```bash
docker-compose up --build
```

- **Backend API**: http://localhost:8000
- **Frontend**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs

## API Endpoints

### Users
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/users` | No | Create user, returns JWT |
| GET | `/users/{id}/token` | No | Get JWT by user ID |
| PATCH | `/users/{id}` | Yes | Update user name |
| DELETE | `/users/{id}` | Yes | Delete user |

### Publications
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/publications` | Yes | Create publication |
| GET | `/publications/user/{id}` | No | Get user's publications (paginated) |
| PATCH | `/publications/{id}` | Yes | Update publication |
| DELETE | `/publications/{id}` | Yes | Delete publication |

## Caching

- Publications are cached in Redis with 600s TTL on creation
- Reading from cache is instant; cache miss triggers a 2s simulated delay before Postgres query
- Cache keys: `pub:{id}`, `user_pubs:{user_id}:{limit}:{offset}`

## Tech Stack

- **Backend**: FastAPI, asyncpg, Redis, PyJWT
- **Frontend**: Vue 3, TypeScript, Vite, Vue Router, Axios
- **Infrastructure**: Docker Compose, PostgreSQL 16, Redis 7

## Postman

Import `backend/postman_collection.json` into Postman. Run "Create User" first to auto-set token and userId variables.
