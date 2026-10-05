'''
In this file will build the market
'''
import pandas as pd

class Market:

    def __init__(self):
        self.market = pd.read_parquet('../data/market_data.parquet')
        self.step = 0
        self.end = False

    def now(self):

        data = self.market.iloc[self.step]
        timestamp = data.name

        return timestamp, data

    def move(self):

        self.step += 1

        if self.step == len(self.market):
            self.end = True
