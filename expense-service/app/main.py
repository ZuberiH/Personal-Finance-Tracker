from fastapi import FastAPI
from app.routes import router
from app.database import create_tables

app = FastAPI()

# Include routes
app.include_router(router)

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/")
def root():
    return {"message": "Expense Tracking Service Running"}
