from fastapi import FastAPI
from app.api.routes import images, auth
from db.session import engine
from db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Image Upload Service", version='0.1')

app.include_router(auth.router)
app.include_router(images.router)
