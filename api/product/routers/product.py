from fastapi import APIRouter, Depends, Form, status, Response, HTTPException
from ..database import get_db
from sqlalchemy.orm import Session
from ..import models, schemas
from typing import List

router = APIRouter()



@router.delete('/product/{id}', tags=['Products'])
def delete(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return{"Product is deleted"}


@router.get('/products', response_model=List[schemas.DisplayProduct], tags=['Products'])
def getproducts(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get('/product/{id}', response_model=schemas.DisplayProduct, tags=['Products'])
def product(id, db: Session = Depends(get_db)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Product is not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Product not found'}
     return product

@router.put('/product/{id}', tags=['Products'])
def update(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    # db.refresh(product)
    return {'Product successfully updated'}
    # return {product}


# @app.post('/product', status_code=status.HTTP_201_CREATED)
@router.post('/product',response_model=schemas.DisplayProduct, 
            status_code=status.HTTP_201_CREATED,tags=['Products'])
def add(request: schemas.Product, db:Session = Depends(get_db)):
    new_product = models.Product(
        name= request.name, description= request.description, price= request.price, seller_id= 1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product