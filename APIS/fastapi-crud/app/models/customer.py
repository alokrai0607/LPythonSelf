from sqlalchemy import Column, Integer, String
from app.config.database import Base

# Define the Customer class as a model that maps to the "customers" table in the database
class Customer(Base):
    # Specify the table name as "customers" in the database
    __tablename__ = "customers"

    # Define the "id" column as an Integer, which is the primary key and should have an index for faster lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # Define the "name" column as a String with a maximum length of 255 characters, and it cannot be null
    name = Column(String(255), nullable=False)
    
    # Define the "email" column as a String with a maximum length of 255 characters, it must be unique across the table, and it should have an index for faster searches
    email = Column(String(255), unique=True, index=True)
    
    # Define the "age" column as an Integer, and it cannot be null
    age = Column(Integer, nullable=False)
