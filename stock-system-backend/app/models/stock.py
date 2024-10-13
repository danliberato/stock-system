from pydantic import BaseModel
from typing import List

class Stock(BaseModel):
    id: int
    quantity: int
    url: str
    ticker_name: str
    ticker: str
    avg_price: float
    current_price: float
    appreciation: float
    avg_rating: str

class StockResponse(BaseModel):
    total: int
    data: List[Stock]
