from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product, seller



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

models.Base.metadata.create_all(engine)

app.include_router(product.router)

app.include_router(seller.router)