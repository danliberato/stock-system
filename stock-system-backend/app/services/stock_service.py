from models.stock import StockResponse, Stock

# Example data; replace with database calls or external API calls
mock_data = StockResponse(
    total=2,
    data=[
        Stock(
            id=5798975,
            quantity=210,
            url="https://investidor10.com.br/acoes/wege3/",
            ticker_name="WEGE3",
            ticker="<span class='hidden'>WEGE3</span>",
            avg_price=36.75,
            current_price=54.17,
            appreciation=47.38,
            avg_rating="<i class='fas fa-fw fa-star' style='color: #D3B583'></i>"
        ),
        Stock(
            id=5956826,
            quantity=289,
            url="https://investidor10.com.br/acoes/itub4/",
            ticker_name="ITUB4",
            ticker="<span class='hidden'>ITUB4</span>",
            avg_price=32.56,
            current_price=34.63,
            appreciation=6.36,
            avg_rating="<i class='fas fa-fw fa-star' style='color: #D3B583'></i>"
        )
    ]
)

async def get_stocks() -> StockResponse:
    return mock_data
