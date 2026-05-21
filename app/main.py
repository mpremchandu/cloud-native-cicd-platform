from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cloud Native CI/CD Platform"}

@app.get("/health")
def health():
    return {"status": "healthy"}
