from pydantic import BaseModel

class BacktestRequest(BaseModel):
    ticker: str
    start_date: str
    end_date: str
    strategy: str
    fast_period: int = 10
    slow_period: int = 30
    cash: float = 100000