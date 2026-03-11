from fastapi import FastAPI
from models.request_models import BacktestRequest
from engine.backtest_engine import run_backtest

app = FastAPI()

@app.get("/")
def home():

    return {"message":"Algo Trading Backtest API"}

@app.post("/run_backtest")

def run_strategy(request:BacktestRequest):

    result = run_backtest(request)

    return result


# python -m uvicorn main:app --reload