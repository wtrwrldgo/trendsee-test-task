from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import close_pool, create_pool
from app.publications.router import router as publications_router
from app.redis_client import close_redis, create_redis
from app.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_pool()
    await create_redis()
    yield
    await close_pool()
    await close_redis()


app = FastAPI(title="Trendsee Publications API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(publications_router, prefix="/publications", tags=["Publications"])


@app.get("/health")
async def health():
    return {"status": "ok"}
