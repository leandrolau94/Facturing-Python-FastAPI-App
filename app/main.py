from fastapi import FastAPI
from app.database import engine, Base

from app.models import user, invoice
from app.routes import auth, invoice

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(invoice.router)

@app.get("/")
def root():
    return {"message": "API de Facturación funcionando"}