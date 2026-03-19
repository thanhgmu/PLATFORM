from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine

from app.api.v1.agents import router as agents_router
from app.api.v1.approvals import router as approvals_router
from app.api.v1.cases import router as cases_router
from app.api.v1.execution_audit import router as execution_audit_router
from app.api.v1.orchestration import router as orchestration_router
from app.api.v1.shared_context import router as shared_context_router

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


app.include_router(cases_router)
app.include_router(agents_router)
app.include_router(orchestration_router)
app.include_router(approvals_router)
app.include_router(shared_context_router)
app.include_router(execution_audit_router)
