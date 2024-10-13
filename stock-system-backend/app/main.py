from fastapi import FastAPI
from routes import stock

app = FastAPI()

print("EXAMPLE!!!")

app.include_router(stock.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)