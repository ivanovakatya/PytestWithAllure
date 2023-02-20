from fastapi import Form
from pydantic import BaseModel


class Product(BaseModel):
    name: str 
    description: str
    price: int
    # seller_id: int



class Seller(BaseModel):
    username: str
    email: str
    password: str

class DisplaySeller(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        orm_mode = True  

class DisplayProduct(BaseModel):
    id: int
    name: str
    description: str
    price: int
    sellers: DisplaySeller
    class Config:
        orm_mode = True





