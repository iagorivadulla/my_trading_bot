from src.account import Account
from src.markets import Market, read_market
from pathlib import Path

def fifty_bucks_every_month(monkey, market, reinvest = False):

    last_month = None

    while not market.end:

        date, prices = market.now()

        ticker = prices.index[0][1]
        price_today = prices.iloc[0]

        if prices['Dividends'].iloc[0]:
            monkey.add_fiat(prices['Dividends'].iloc[0] * monkey.assets[ticker]['amount'])
            print(f'{ticker} has paid {prices['Dividends'].iloc[0] * monkey.assets[ticker]['amount']} USD.')


        if last_month != date.month:
            monkey.add_fiat(100) #every month gets 50 bucks

            if reinvest:
                amount = monkey.fiat/price_today
            else:
                amount = 100 / price_today

            monkey.buy(asset=ticker, amount=amount, price=prices.iloc[0], date=date)

            last_month = date.month

        market.move()


