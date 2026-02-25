from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="FastAPI Backend Mastery",
    description="Phase 1 - Core API Foundation",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "FastAPI Backend Mastery Started 🚀"}

app.include_router(router)