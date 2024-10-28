import ctypes, os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

CLIENT = MongoClient(os.getenv('CLIENT'))
REAL_ESTATE_DATABASE = os.getenv("REAL_ESTATE_DATABASE")
HOUSE_COLLECTION = os.getenv('HOUSE_COLLECTION')
HOUSE_COLLECTION = f'{CLIENT}[{REAL_ESTATE_DATABASE}][{HOUSE_COLLECTION}]'

test = HOUSE_COLLECTION.find('')
print(test)

mylib = ctypes.CDLL('./lib.dylib')

mylib.hello()