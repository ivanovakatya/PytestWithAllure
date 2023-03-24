from fastapi import APIRouter, Depends, Form, status, Response, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from ..import models, schemas
from typing import List
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

@router.post('/seller', response_model=schemas.DisplaySeller, tags=['Sellers'])
def create_seller(request: schemas.Seller, db:Session = Depends(get_db)):
    hash_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username = request.username, email = request.email, password = hash_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller