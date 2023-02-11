from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from uuid import UUID
from datetime import date, datetime, time, timedelta

app = FastAPI()


class Profile(BaseModel):
    name: str
    email: str
    age: int

class Image(BaseModel):
    url: HttpUrl
    name: str

class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    execute_after: timedelta


class Product(BaseModel):
    name: str = Field(example= "phone")
# Defining the attributes of the class
    price: int = Field(title= "Price of the item",
                        description= "This would be the price of the item being added")
    discount: int
    image: List[Image]

# To define the sample data for the route
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Phone",
    #         "price": 100,
    #         "discount": 0,
    #         "image": [
    #             {"url": "https://www.google.com",
    #             "name": "google image"},
    #             {"url": "https://www.google.com",
    #             "name": "phone image side view"},
    #         ]
    #         }
    #     }



class Offer(BaseModel):
# Defining the example data here
    name: str = Field(example= "phone")
    description: str
    price: float
    products: List[Product]


class User(BaseModel):
    name: str
    email: str


@app.get('/')
def index():
    return {'Hello world'}

@app.post('/addoffer')
def addoffer(offer: Offer):
    return {offer}


@app.post('/addevent')
def addevent(event: Event):
    return {event}


@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}