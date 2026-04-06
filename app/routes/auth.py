from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="auth", tags=["Auth"])

# DataBase dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register
# this function looks for a registered user, is the user is not registered
# it creates a new user with his email and password
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Usuario creado correctamente"}

# Login
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales invalidas")
    
    token = create_access_token({"sub": db_user.email})
    
    return {"access_token": token, "token_type": "bearer"}