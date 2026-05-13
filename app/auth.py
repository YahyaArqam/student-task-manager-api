from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

from app import models, schemas
from app.database import get_db

# Load .env file
load_dotenv()

# Read values from .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# This handles password hashing
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# This tells FastAPI where to look for token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ─────────────────────────────
# PASSWORD FUNCTIONS
# ─────────────────────────────

# Turn plain password into hashed password
def hash_password(password: str):
    return pwd_context.hash(password)

# Check if plain password matches hashed password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# ─────────────────────────────
# JWT TOKEN FUNCTIONS
# ─────────────────────────────

# Create a JWT token
def create_access_token(data: dict):
    to_encode = data.copy()

    # Token expires after X minutes
    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    # Create the token
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return encoded_jwt


# ─────────────────────────────
# GET CURRENT USER
# ─────────────────────────────

# This checks token and returns logged in user
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode the token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        # Get email from token
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    # Find user in database
    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user


# ─────────────────────────────
# ADMIN CHECK
# ─────────────────────────────

# This checks if user is admin
def get_admin_user(
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins only!"
        )
    return current_user