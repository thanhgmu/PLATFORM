import time
from sqlalchemy import create_engine, text
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, future=True)
max_attempts = 30

for attempt in range(1, max_attempts + 1):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("[platform] database is ready")
        raise SystemExit(0)
    except Exception as exc:
        print(f"[platform] db not ready (attempt {attempt}/{max_attempts}): {exc}")
        time.sleep(2)

raise SystemExit("[platform] database did not become ready in time")
