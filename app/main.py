from fastapi import FastAPI
from app.routes.tasks import router as task_router

app = FastAPI()

app.include_router(task_router)

@app.get("/")
def home():
    return {"message": "Cloud Native CI/CD Platform"}

@app.get("/health")
def health():
    return {"status": "healthy"}
