from sqlalchemy.orm import Session
from app.models.customer import Customer

# This class handles all database operations related to the Customer model
class CustomerRepository:

    # Static method to retrieve all customers from the database
    @staticmethod
    def get_all_customers(db: Session):
        # Query the Customer table and return a list of all customers
        return db.query(Customer).all()

    # Static method to retrieve a customer by their ID
    @staticmethod
    def get_customer_by_id(db: Session, customer_id: int):
        # Query the Customer table, filter by the provided customer_id, and return the first match (or None if not found)
        return db.query(Customer).filter(Customer.id == customer_id).first()

    # Static method to create a new customer record in the database
    @staticmethod
    def create_customer(db: Session, customer: Customer):
        # Add the new Customer object to the session, marking it for insertion into the database
        db.add(customer)
        # Commit the session to save the changes, which inserts the new customer into the database
        db.commit()
        # Refresh the customer object to reflect any changes made by the database (e.g., auto-generated ID)
        db.refresh(customer)
        # Return the newly created customer object, now containing any database-generated fields
        return customer

    # Static method to update an existing customer record in the database
    @staticmethod
    def update_customer(db: Session, customer_id: int, updated_customer: Customer):
        # Retrieve the existing customer by their ID
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        # If the customer exists, update the customer's details with the new data
        if customer:
            # Update the customer's name with the new name from the updated_customer object
            customer.name = updated_customer.name
            # Update the customer's email with the new email from the updated_customer object
            customer.email = updated_customer.email
            # Update the customer's age with the new age from the updated_customer object
            customer.age = updated_customer.age
            # Commit the session to save the changes, updating the customer's record in the database
            db.commit()
            # Refresh the customer object to reflect the latest state in the database
            db.refresh(customer)
        # Return the updated customer object
        return customer

    # Static method to delete a customer record from the database by their ID
    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        # Retrieve the customer by their ID
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        # If the customer exists, delete the record from the database
        if customer:
            # Mark the customer object for deletion from the session
            db.delete(customer)
            # Commit the session to finalize the deletion in the database
            db.commit()
        # Return the deleted customer object (or None if not found), mainly for confirmation purposes
        return customer
