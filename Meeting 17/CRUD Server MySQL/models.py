from sqlalchemy import Boolean, Column, Integer, String, DECIMAL
from database import Base


class Customer(Base):
    __tablename__ = 'customers'

    customerNumber = Column(Integer, primary_key=True, index=True)
    customerName = Column(String(50))
    contactLastName = Column(String(50))
    contactFirstName = Column(String(50))
    phone = Column(String(50))
    addressLine1 = Column(String(50))
    addressLine2 = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    postalCode = Column(String(15))
    country = Column(String(50))
    salesRepEmployeeNumber = Column(Integer, foreign_key=True)
    creditLimit = Column(DECIMAL(10, 2))
