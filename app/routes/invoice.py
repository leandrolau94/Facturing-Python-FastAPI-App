from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate
from app.core.deps import get_current_user

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint para hacer post y crear factura
@router.post("/")
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_invoice = Invoice(
        amount=invoice.amount,
        status="pending",
        user_id=current_user.id
    )
    
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    
    return new_invoice

# endpoint para obtener facturas
@router.get("/")
def get_invoices(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    invoices = db.query(Invoice).filter(Invoice.user_id == current_user.id).all()
    return invoices

# endpoint para cambiar estado de factura con put request
@router.put("/{invoice_id}")
def update_invoice_status(
    invoice_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id,
        Invoice.user_id == current_user.id).first()
    
    if not invoice:
        raise HTTPException(
            status_code=401,
            detail="Factura no encontrada"
        )
    
    invoice.status = status
    
    db.commit()
    db.refresh(invoice)
    
    return invoice