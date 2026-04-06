from fastapi import APIRouter, Depends
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.get("/")
def get_invoices(current_user: str = Depends(get_current_user)):
    return {"message": f"Invoices para {current_user}"}