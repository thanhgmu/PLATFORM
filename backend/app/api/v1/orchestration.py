from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.orchestration import OrchestrationRunCreate, OrchestrationRunRead
from app.services.orchestration.orchestration_engine import OrchestrationEngine

router = APIRouter(prefix="/orchestration", tags=["orchestration"])
engine = OrchestrationEngine()


@router.post("/runs", response_model=OrchestrationRunRead)
def create_run(payload: OrchestrationRunCreate, db: Session = Depends(get_db)):
    return engine.create_run(db, payload)


@router.get("/runs/{run_id}", response_model=OrchestrationRunRead)
def get_run(run_id: int, db: Session = Depends(get_db)):
    item = engine.get_run(db, run_id)
    if not item:
        raise HTTPException(status_code=404, detail="Run not found")
    return item


@router.post("/runs/{run_id}/cancel", response_model=OrchestrationRunRead)
def cancel_run(run_id: int, db: Session = Depends(get_db)):
    item = engine.cancel_run(db, run_id)
    if not item:
        raise HTTPException(status_code=404, detail="Run not found")
    return item
