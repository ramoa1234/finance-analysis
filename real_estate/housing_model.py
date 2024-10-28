from dotenv import load_dotenv
from pymongo import MongoClient
import os, requests, json

load_dotenv()

CLIENT = MongoClient(os.getenv('CLIENT'))
REAL_ESTATE_DATABASE = os.getenv("REAL_ESTATE_DATABASE")
HOUSE_COLLECTION = os.getenv('HOUSE_COLLECTION')
APARTMENT_COLLECTION = os.getenv('APARTMENT_COLLECTION')
HOUSE_COLLECTION = f'{CLIENT}[{REAL_ESTATE_DATABASE}][{HOUSE_COLLECTION}]'
APARTMENT_COLLECTION = f'{CLIENT}[{REAL_ESTATE_DATABASE}][{APARTMENT_COLLECTION}]'
 

def address_object(address, zip_code, state, city, county):
    address_data = {
        "address": address,
        "zip_code": zip_code,
        "state": state,
        "city": city,   
        "county": county
    }
    return address_data

#check if the value that is going to be taken in has the minimum needed to be added
class Housing:
    def __init__(self, housing_type, address, status, bedrooms, bathrooms, price, property_id, data_bought, under_construction, square_feet, list_data):
        if address and bedrooms and bathrooms and price:
            self.housing_type = housing_type
            self.address = address
            self.status = status
            self.bedrooms = bedrooms
            self.bathroom = bathrooms
            self.price = price
            self.property_id = property_id
            self.date_bought = data_bought
            self.under_construction = under_construction
            self.square_feet = square_feet
            self.list_data = list_data
        else:
            #need to update to speicfy error type
            raise ValueError("All parameters must be provided")

    def save_to_houses(self): 
        document = {
            "housing_type": self.housing_type,
            "address": self.address,
            "status": self.status,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "price": self.price,
            "property_id": self.property_id,
            "data_bought": self.date_bought,
            "under_construction": self.under_construction,
            "square_feet": self.square_feet,
            "list_data": self.list_data
        }
        result = HOUSE_COLLECTION.insert_one(document)
        print(f"Inserted house with id: {result.inserted_id}")

    def save_to_apartments():
        def save_to_apartments(self):
            document = {
                "housing_type": self.housing_type,
                "address": self.address,
                "rooms": self.rooms,
                "bedrooms": self.bedrooms,
                "price": self.price,
                "location": self.location
            }
            result = APARTMENT_COLLECTION.insert_one(document)
            print(f"Inserted apartment with id: {result.inserted_id}")

def append_to_db(property):
    pass