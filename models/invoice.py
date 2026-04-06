from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    status = Column(String, default="pending")
    
    user_id = Column(Integer, ForeignKey("users.id"))