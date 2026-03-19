from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

# Comment những router không có file thật trong backend/app/api/v1
# from app.api.v1.auth import router as auth_router
# from app.api.v1.tenants import router as tenants_router
# from app.api.v1.plugins import router as plugins_router
# from app.api.v1.marketplace import router as marketplace_router
# from app.api.v1.openclaw import router as openclaw_router
# from app.api.v1.consent import router as consent_router
# from app.api.v1.behavior import router as behavior_router

from app.api.v1.cases import router as cases_router
from app.api.v1.agents import router as agents_router
from app.api.v1.orchestration import router as orchestration_router
from app.api.v1.approvals import router as approvals_router
from app.api.v1.shared_context import router as shared_context_router
from app.api.v1.execution_audit import router as execution_audit_router

app = FastAPI(title="Platform Core")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/")
def root():
    return {"service": "platform-core"}


# app.include_router(auth_router)
# app.include_router(tenants_router)
# app.include_router(plugins_router)
# app.include_router(marketplace_router)
# app.include_router(openclaw_router)
# app.include_router(consent_router)
# app.include_router(behavior_router)

app.include_router(cases_router)
app.include_router(agents_router)
app.include_router(orchestration_router)
app.include_router(approvals_router)
app.include_router(shared_context_router)
app.include_router(execution_audit_router)
