from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    amount: int

class InvoiceResponse(BaseModel):
    id: int
    amount: int
    status: str
    
    class Config:
        from_attributes = True