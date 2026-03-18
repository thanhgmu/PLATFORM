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

    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
    QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
    FLOWISE_URL = os.getenv("FLOWISE_URL", "http://flowise:3000")
    SHARED_CONTEXT_INDEX_PROVIDER = os.getenv("SHARED_CONTEXT_INDEX_PROVIDER", "qdrant")
    ORCHESTRATION_MAX_STEPS = int(os.getenv("ORCHESTRATION_MAX_STEPS", "12"))
    APPROVAL_TTL_MINUTES = int(os.getenv("APPROVAL_TTL_MINUTES", "1440"))
    TENANT_ENFORCE_ISOLATION = os.getenv("TENANT_ENFORCE_ISOLATION", "true").lower() == "true"

    SUPERADMIN_EMAIL = os.getenv("SUPERADMIN_EMAIL", "admin@example.com")
    SUPERADMIN_PASSWORD = os.getenv("SUPERADMIN_PASSWORD", "ChangeMe123!")


settings = Settings()
