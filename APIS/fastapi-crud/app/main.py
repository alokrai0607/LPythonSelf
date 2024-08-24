from fastapi import FastAPI
from app.config.database import engine, Base
from app.controllers.customer_controller import router as customer_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "FastAPI CRUD application is working fine"}

app.include_router(customer_router, prefix="/api")


# 1.	Activate the virtual environment:

# venv\Scripts\activate

# 2.	 Install the Required MySQL Connector:

# pip install mysql-connector-python

# 3.	Running the FastAPI Application:

# uvicorn app.main:app --reload
