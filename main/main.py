from fastapi import FastAPI

PORT = 3000

app = FastAPI()

@app.get('/api')
async def main():
    return {"mesage": "hello, world"}
    
