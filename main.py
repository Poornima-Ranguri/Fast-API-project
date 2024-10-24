# Import FastAPI from fastapi
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a route that returns "Hello, World!"
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
