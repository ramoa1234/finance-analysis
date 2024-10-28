from fastapi import FastAPI
from dotenv import load_dotenv
from housing_model import Housing
import os, requests

app = FastAPI()
load_dotenv()
LOCALHOST_URL = os.getenv('LOCALHOST_URL')
PORT = os.getenv("PORT")
print(f'listing on port {PORT}')

errors = []
@app.post('/errors')
async def all_errors(errors):
    error_message = errors.error_message
    errors.append(error_message)

@app.post("/api/real_estate")
async def add_to_db(housing: dict):
    if not housing.address:
        error_message ="error incoming data had no address"
        requests.get(str(f'{LOCALHOST_URL}/errors', error_message))
    if not housing.rooms:
        error_message = "error number of rooms not given"
    if not housing.bathrooms:
        error_message ="number of bathrooms not given"
        requests.get(str(f'{LOCALHOST_URL}/errors', error_message))
    if not housing.price:
        error_message ="error price of the house not given"
        requests.get(str(f'{LOCALHOST_URL}/errors', error_message))
   
    