from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.customer_service import CustomerService
from app.config.database import get_db
from pydantic import BaseModel

# Create a new APIRouter instance to define customer-related routes.
router = APIRouter()

# Define a Pydantic model for creating a new customer.
class CustomerCreate(BaseModel):
    name: str   
    email: str
    age: int

# Define a route to get all customers with optional pagination.
@router.get("/customers/")
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    # Initialize the CustomerService with the current database session.
    service = CustomerService(db)
    # Fetch all customers using the service, ignoring the pagination arguments for now.
    customers = service.get_all_customers()
    # Return the list of customers.
    return customers

# Define a route to get a single customer by their ID.
@router.get("/customers/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    # Initialize the CustomerService with the current database session.
    service = CustomerService(db)
    # Fetch the customer by ID using the service.
    customer = service.get_customer_by_id(customer_id)
    # If the customer is not found, raise a 404 HTTP exception.
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    # Return the customer data.
    return customer

# Define a route to create a new customer.
@router.post("/customers/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    # Initialize the CustomerService with the current database session.
    service = CustomerService(db)
    # Call the service method to create a new customer with the provided data.
    return service.create_customer(customer.name, customer.email, customer.age)

# Define a route to update an existing customer by their ID.
@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, name: str, email: str, age: int, db: Session = Depends(get_db)):
    # Initialize the CustomerService with the current database session.
    service = CustomerService(db)
    # Call the service method to update the customer with the provided ID and new data.
    return service.update_customer(customer_id, name, email, age)

# Define a route to delete a customer by their ID.
@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    # Initialize the CustomerService with the current database session.
    service = CustomerService(db)
    # Call the service method to delete the customer with the provided ID.
    return service.delete_customer(customer_id)
