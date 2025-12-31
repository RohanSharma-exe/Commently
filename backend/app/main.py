from fastapi import FastAPI
from app.api.auth.routes import router as auth_router
from app.api.health.routes import router as health_router
from app.core.database import engine, Base
from app.models.user import User

app = FastAPI(title="Instagram Automation SaaS")

app.include_router(auth_router)
app.include_router(health_router)

Base.metadata.create_all(bind=engine)
