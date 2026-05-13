from fastapi import FastAPI
from app.database import engine, Base
from app.routers import users, tasks

# ✅ Create all database tables
Base.metadata.create_all(bind=engine)

# ✅ Create FastAPI app
app = FastAPI(
    title="Student Task Manager API",
    description="Authentication and Authorization Demo",
    version="1.0.0"
)

# ✅ Connect routers
app.include_router(users.router)
app.include_router(tasks.router)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Welcome to Student Task Manager API 🚀"}