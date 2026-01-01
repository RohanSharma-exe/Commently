from fastapi import FastAPI
from app.api.auth.routes import router as auth_router
from app.api.health.routes import router as health_router
from app.api.users.routes import router as users_router
from app.models.instagram_account import InstagramAccount
from app.api.instagram.routes import router as instagram_router

from app.core.database import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Commently")  # or your chosen name

app.include_router(auth_router)
app.include_router(health_router)
app.include_router(users_router)
app.include_router(instagram_router)
