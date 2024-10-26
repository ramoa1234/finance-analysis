from fastapi import FastAPI

app = FastAPI()

app.post('/api/real_estate')
async def get_home_item(house_schame):
    
    
    return {
        "address": house_schema.address,
        "price": home_price
    }
