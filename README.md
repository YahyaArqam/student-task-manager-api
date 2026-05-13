# Student Task Manager API

A FastAPI backend application demonstrating Authentication and Authorization using JWT and Role-Based Access Control.

## 🚀 Features

- User Registration
- User Login (JWT Authentication)
- Password Hashing
- Protected Routes
- Role-Based Authorization (Admin only routes)
- Task CRUD Operations
- PostgreSQL Database (Neon)
- SQLAlchemy ORM

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL (Neon)
- SQLAlchemy
- JWT (python-jose)
- Passlib

## 📦 Installation

1. Clone repository

2. Create virtual environment
3. Activate virtual environment
4. Install dependencies
5. Create `.env` file and add:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

6. Run server
uvicorn app.main:app --reload
## 📘 API Docs

Visit:
http://127.0.0.1:8000/docs


## 🔐 Authentication Flow

1. Register user
2. Login to receive JWT token
3. Use token to access protected routes
4. Admin users can access admin-only endpoints

---

Built for Backend Assignment