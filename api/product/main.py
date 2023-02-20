from fastapi import FastAPI, Depends, Form, status, Response, HTTPException
from .import schemas
from .import models
from .database import engine, SessionLocal
from typing import List
from passlib.context import CryptContext



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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@app.delete('/product/{id}', tags=['Products'])
def delete(id, db: SessionLocal = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return{"Product is deleted"}


@app.get('/products', response_model=List[schemas.DisplayProduct], tags=['Products'])
def getproducts(db: SessionLocal = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}', response_model=schemas.DisplayProduct, tags=['Products'])
def product(id, db: SessionLocal = Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Product is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Product not found'}
     return product

@app.put('/product/{id}', tags=['Products'])
def update(id, request: schemas.Product, db: SessionLocal = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    # db.refresh(product)
    return {'Product successfully updated'}
    # return {product}


# @app.post('/product', status_code=status.HTTP_201_CREATED)
@app.post('/product',response_model=schemas.DisplayProduct, 
            status_code=status.HTTP_201_CREATED,tags=['Products'])
def add(request: schemas.Product, db:SessionLocal = Depends(get_db)):
    new_product = models.Product(
        name= request.name, description= request.description, price= request.price, seller_id= 1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

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