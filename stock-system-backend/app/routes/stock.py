from fastapi import APIRouter
from models.stock import StockResponse
from services.stock_service import get_stocks

router = APIRouter()

@router.get("/stocks", response_model=StockResponse)
async def fetch_stocks():
    return await get_stocks()
