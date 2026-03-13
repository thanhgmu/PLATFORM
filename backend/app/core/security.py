from datetime import datetime, timedelta, timezone
from hashlib import sha256
import base64
import hmac
import json

from app.core.config import settings

def hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def create_access_token(subject: str) -> str:
    payload = {
        "sub": subject,
        "exp": int((datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp())
    }
    header = {"alg": "HS256", "typ": "JWT"}

    def b64(data: dict) -> str:
        raw = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
        return base64.urlsafe_b64encode(raw).decode("utf-8").rstrip("=")

    signing_input = f"{b64(header)}.{b64(payload)}"
    signature = hmac.new(
        settings.SECRET_KEY.encode("utf-8"),
        signing_input.encode("utf-8"),
        digestmod="sha256",
    ).digest()
    signature_b64 = base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")
    return f"{signing_input}.{signature_b64}"
