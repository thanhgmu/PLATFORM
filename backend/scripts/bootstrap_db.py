from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import hash_password
from app.db.base import Base
from app.db.session import engine, SessionLocal
import app.models  # noqa: F401
from app.models.user import User
from app.services.plugin_loader import scan_plugins, sync_plugins_to_db

Base.metadata.create_all(bind=engine)

db: Session = SessionLocal()
try:
    admin = db.query(User).filter(User.email == settings.SUPERADMIN_EMAIL).first()
    if not admin:
        admin = User(
            email=settings.SUPERADMIN_EMAIL,
            hashed_password=hash_password(settings.SUPERADMIN_PASSWORD),
            role="admin",
        )
        db.add(admin)
        db.commit()
        print(f"[platform] seeded admin user: {settings.SUPERADMIN_EMAIL}")
    else:
        print(f"[platform] admin user already exists: {settings.SUPERADMIN_EMAIL}")

    discovered = scan_plugins()
    sync_plugins_to_db(db, discovered)
    print(f"[platform] synced plugins: {[p['slug'] for p in discovered]}")
finally:
    db.close()
