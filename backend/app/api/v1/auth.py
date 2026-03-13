from fastapi import APIRouter
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.core.security import create_access_token, hash_password

router = APIRouter()

@router.post("/register", response_model=TokenResponse)
def register(payload: RegisterRequest):
    _ = hash_password(payload.password)
    token = create_access_token(payload.email)
    return TokenResponse(access_token=token)

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    token = create_access_token(payload.email)
    return TokenResponse(access_token=token)

@router.get("/me")
def me():
    return {"email": "admin@example.com", "role": "admin"}
