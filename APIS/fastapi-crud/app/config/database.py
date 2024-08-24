from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#I am Writing database url here with my login id and password & database name .
DATABASE_URL = "mysql+mysqlconnector://root:0303@localhost:3306/fastapi_crud"

#create_engine is a function provided by SQLAlchemy to create an instance of the Engine class.
engine = create_engine(DATABASE_URL)

# sessionmaker is a factory function in SQLAlchemy for creating Session objects.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base is a function provided by SQLAlchemy that creates a base class for declarative class definitions.
Base = declarative_base()


def get_db():
    #This line creates a new Session object using the SessionLocal factory.
    db = SessionLocal()
    try:
        # yield is used to produce a value in a generator function.
        yield db
        #This starts a finally block which executes code regardless of whether an exception occurred or not.
    finally:
        #It ensures that the db.close() method is called to clean up and close the database session properly.
        db.close()
