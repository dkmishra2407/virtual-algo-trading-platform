import backtrader as bt
import yfinance as yf
from strategies.sma_strategy import SMAStrategy

def run_backtest(params):

    data = yf.download(
        params.ticker,
        start=params.start_date,
        end=params.end_date,
        auto_adjust=True
    )

    data.columns = [col[0] if isinstance(col,tuple) else col for col in data.columns]

    cerebro = bt.Cerebro()

    cerebro.broker.setcash(params.cash)

    cerebro.addstrategy(
        SMAStrategy,
        fast=params.fast_period,
        slow=params.slow_period
    )

    datafeed = bt.feeds.PandasData(dataname=data)

    cerebro.adddata(datafeed)

    result = cerebro.run()

    final_value = cerebro.broker.getvalue()

    strategy = result[0]
    cerebro.plot()
    return {
        "final_portfolio_value":final_value,
        "trade_log":strategy.trade_log
    }