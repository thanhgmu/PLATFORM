import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Platform Core")
    ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./platform.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

    STORAGE_PROVIDER = os.getenv("STORAGE_PROVIDER", "minio")
    STORAGE_BUCKET = os.getenv("STORAGE_BUCKET", "platform")
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://minio:9000")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minio")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minio123")

    S3_ENDPOINT = os.getenv("S3_ENDPOINT", "https://s3.example.com")
    S3_BUCKET = os.getenv("S3_BUCKET", "platform")
    S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY", "change-me")
    S3_SECRET_KEY = os.getenv("S3_SECRET_KEY", "change-me")

    WEBDAV_BASE_URL = os.getenv("WEBDAV_BASE_URL", "https://webdav.example.com")
    WEBDAV_USERNAME = os.getenv("WEBDAV_USERNAME", "change-me")
    WEBDAV_PASSWORD = os.getenv("WEBDAV_PASSWORD", "change-me")

    OPENCLAW_BASE_URL = os.getenv("OPENCLAW_BASE_URL", "http://openclaw:8080")
    OPENCLAW_ENABLED = os.getenv("OPENCLAW_ENABLED", "false").lower() == "true"

settings = Settings()
