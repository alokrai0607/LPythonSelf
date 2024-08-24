from sqlalchemy.orm import Session
from app.repositories.customer_repository import CustomerRepository
from app.models.customer import Customer

# The CustomerService class provides a higher-level abstraction for customer-related operations.
# It handles the business logic and delegates database operations to the CustomerRepository.
class CustomerService:

    # The constructor initializes the service with a database session.
    def __init__(self, db: Session):
        # Store the provided database session to be used in service methods.
        self.db = db
        # Instantiate the CustomerRepository to handle actual database operations.
        self.repository = CustomerRepository()

    # Method to retrieve all customers from the database.
    def get_all_customers(self):
        # Call the repository method to fetch all customers, passing the database session.
        return self.repository.get_all_customers(self.db)

    # Method to retrieve a specific customer by their ID.
    def get_customer_by_id(self, customer_id: int):
        # Call the repository method to fetch a customer by ID, passing the database session and customer ID.
        return self.repository.get_customer_by_id(self.db, customer_id)

    # Method to create a new customer record in the database.
    def create_customer(self, name: str, email: str, age: int):
        # Create a new Customer object with the provided name, email, and age.
        new_customer = Customer(name=name, email=email, age=age)
        # Call the repository method to insert the new customer into the database.
        return self.repository.create_customer(self.db, new_customer)

    # Method to update an existing customer record in the database.
    def update_customer(self, customer_id: int, name: str, email: str, age: int):
        # Create a Customer object with the updated data, including the customer ID.
        updated_customer = Customer(id=customer_id, name=name, email=email, age=age)
        # Call the repository method to update the existing customer record in the database.
        return self.repository.update_customer(self.db, customer_id, updated_customer)

    # Method to delete a customer record by their ID.
    def delete_customer(self, customer_id: int):
        # Call the repository method to delete the customer record from the database.
        return self.repository.delete_customer(self.db, customer_id)
