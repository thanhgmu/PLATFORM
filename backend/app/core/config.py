import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Platform Core")
    ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./platform.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

settings = Settings()
