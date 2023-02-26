from fastapi import FastAPI, Depends, Form, status, Response, HTTPException
from .import schemas
from .import models
from .database import engine, SessionLocal, get_db
from typing import List
from passlib.context import CryptContext
from .routers import product



app = FastAPI(
    title = "Products Api",
    description = "Get details for all products on our website",
    terms_of_service = "https://www.google.com",
    contact = {
        "Developer name": ["Indu", "Kate"],
        "Website": "https://www.google.com",
        "email": "Fastapi@gmail.com",
    },
    license_info = {
        "name": "XYZ",
        "url": "https://www.google.com",
    },
# docs_url with update the url and redoc_url = None will disable the redoc documentation
    # docs_url = '/documentation', 
    # redoc_url = None
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

models.Base.metadata.create_all(engine)

app.include_router(product.router)




@app.post('/seller', response_model=schemas.DisplaySeller, tags=['Sellers'])
def create_seller(request: schemas.Seller, db:SessionLocal = Depends(get_db)):
    hash_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username = request.username, email = request.email, password = hash_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller