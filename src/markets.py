'''
In this file will build the market
'''
import pandas as pd

class Market:

    def __init__(self, market_data: str):
        self.market = pd.read_parquet(market_data)
        self.step = 0
        self.end = False

    def now(self):
        if self.end:
            return None

        data = self.market.iloc[self.step]
        timestamp = data.name

        return timestamp, data

    def move(self):
        self.step += 1
        if self.step == len(self.market):
            self.end = True

    def reset(self):
        self.step = 0
        self.end = False



def read_market(market_data) -> dict:

    tickers = market_data['Close'].index

    market = {}

    for ticker in tickers:
        if market_data['Dividends'][ticker].item() > 0:
            market[ticker] = (market_data['Close'][ticker].item(), market_data['Dividends'][ticker].item())
        else:
            market[ticker] = (market_data['Close'][ticker], None)

    return market