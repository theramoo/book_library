from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import book

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Library API")

app.include_router(book.router)
