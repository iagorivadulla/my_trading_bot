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
