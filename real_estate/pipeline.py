from fastapi import FastAPI
from dotenv import load_dotenv
from housing_model import Housing
from housing_model import append_to_db
from pymongo import MongoClient
import os, requests

app = FastAPI()
load_dotenv()
CLIENT = MongoClient(os.getenv('CLIENT'))
REAL_ESTATE_DATABASE = os.getenv("REAL_ESTATE_DATABASE")
HOUSE_COLLECTION = os.getenv('HOUSE_COLLECTION')
HOUSE_COLLECTION = f'{CLIENT}[{REAL_ESTATE_DATABASE}][{HOUSE_COLLECTION}]'
LOCALHOST_URL = os.getenv('LOCALHOST_URL')
PORT = os.getenv("PORT")
print(f'listing on port {PORT}')

errors = []
@app.post('/errors')
async def all_errors(errors):
    error_message = errors.error_message
    errors.append(error_message)

#pipe line where data has to go through to get added to the database
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

    if housing.type == 'house':
        house = Housing(housing.address, housing.type, housing.address, housing.status, housing.bedrooms, housing.bathrooms, housing.price, housing.property_id, housing.date_bought, housing.under_construction, housing.square_feet, housing.list_data)
        result = HOUSE_COLLECTION.find_one(house)
        if result:
            print('House already exist in db')
        else:
            HOUSE_COLLECTION.insert_one(house.save_to_houses())
            print('new house added to db')