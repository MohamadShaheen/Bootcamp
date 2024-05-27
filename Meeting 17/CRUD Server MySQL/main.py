from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Annotated, Optional
import models
from database import engine, session_local
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class CustomerBase(BaseModel):
    customerNumber: int
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    postalCode: str
    country: str
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: float


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get('/get_customer_id/{customerNumber}', status_code=status.HTTP_200_OK)
async def get_customer_by_id(customerNumber: int, db: db_dependency):
    customer = db.query(models.Customer).filter(models.Customer.customerNumber == customerNumber).first()
    if customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    return customer


@app.get('/get_customer_name/{customerName}', status_code=status.HTTP_200_OK)
async def get_customer_by_name(customerName: str, db: db_dependency):
    customer = db.query(models.Customer).filter(models.Customer.customerName == customerName).first()
    if customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    return customer


@app.post('/add_customer/', status_code=status.HTTP_201_CREATED)
async def add_customer(customer: CustomerBase, db: db_dependency):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()


@app.delete('/delete_customer_id/{customer_id}', status_code=status.HTTP_201_CREATED)
async def delete_customer(customerNumber: int, db: db_dependency):
    db_customer = db.query(models.Customer).filter(models.Customer.customerNumber == customerNumber).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    db.delete(db_customer)
    db.commit()
