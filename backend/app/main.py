from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.tenants import router as tenants_router
from app.api.v1.plugins import router as plugins_router
from app.api.v1.marketplace import router as marketplace_router

app = FastAPI(title="Platform Core")

app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(tenants_router, prefix="/api/v1/tenants", tags=["tenants"])
app.include_router(plugins_router, prefix="/api/v1/plugins", tags=["plugins"])
app.include_router(marketplace_router, prefix="/api/v1/marketplace", tags=["marketplace"])

@app.get("/")
def root():
    return {"status": "ok", "service": "platform-core"}
