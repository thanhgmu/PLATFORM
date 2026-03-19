from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
# from app.api.v1.auth import router as auth_router
# from app.api.v1.tenants import router as tenants_router
# from app.api.v1.plugins import router as plugins_router
from app.api.v1.marketplace import router as marketplace_router
from app.api.v1.openclaw import router as openclaw_router
from app.api.v1.consent import router as consent_router
from app.api.v1.behavior import router as behavior_router
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


# app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
# app.include_router(tenants_router, prefix="/api/v1/tenants", tags=["tenants"])
# app.include_router(plugins_router, prefix="/api/v1/plugins", tags=["plugins"])
app.include_router(marketplace_router, prefix="/api/v1/marketplace", tags=["marketplace"])
app.include_router(openclaw_router, prefix="/api/v1/openclaw", tags=["openclaw"])
app.include_router(consent_router, prefix="/api/v1/consents", tags=["consents"])
app.include_router(behavior_router, prefix="/api/v1/behavior", tags=["behavior"])
app.include_router(cases_router, prefix="/api/v1/cases", tags=["cases"])
app.include_router(agents_router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(orchestration_router, prefix="/api/v1/orchestration", tags=["orchestration"])
app.include_router(approvals_router, prefix="/api/v1/approvals", tags=["approvals"])
app.include_router(shared_context_router, prefix="/api/v1/shared-context", tags=["shared-context"])
app.include_router(execution_audit_router, prefix="/api/v1/execution-audit", tags=["execution-audit"])


@app.get("/")
def root():
    return {"status": "ok", "service": "platform-core"}
