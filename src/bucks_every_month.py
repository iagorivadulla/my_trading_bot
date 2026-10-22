from src.account import Account
from src.markets import Market, read_market
from pathlib import Path

def fifty_bucks_every_month(monkey, market):

    last_month = None

    while not market.end:

        date, prices = market.now()

        if last_month != date.month:
            monkey.add_fiat(50) #every month gets 50 bucks

            ticker = prices.index[0][1]
            price_today = prices.iloc[0]

            amount = 50/price_today

            monkey.buy(asset=ticker, amount=amount, price=prices[0], date=date)

            last_month = date.month

        market.move()


