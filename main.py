from src.account import Account
from src.markets import Market, read_market
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data' / 'market_data.parquet'

market = Market(DATA_DIR)
tickers = list(market.market['Close'].columns)

def random_choice():
    actions = ['buy', 'sell', 'hold']
    global tickers
    return random.choice(actions), random.choice(tickers)

def random_money(monkey):
    total_fiat = monkey.fiat
    return round(random.uniform(1, total_fiat), 2)

def random_amount(monkey, ticker):
    try:

        total_amount = monkey.assets[ticker]['amount']
        return round(random.uniform(1, total_amount), 2)
    except KeyError:
        return None

def trading_monkey(monkey, market):

    while not market.end:
        date, prices = market.now()

        prices = read_market(prices)
        action, ticker = random_choice()
        money = random_money(monkey) / prices[ticker]
        amount = random_amount(monkey, ticker)

        if action == 'buy':
            monkey.buy(asset=ticker, amount = money  ,price=prices[ticker], date=date)

        elif action == 'sell':
            monkey.sell(asset=ticker, amount=amount, price=prices[ticker], date=date)

        elif action == 'hold':
            pass

        market.move()

    print(monkey.state)
    print(monkey.hist)

if __name__ == '__main__':
    monkey = Account(5000)
    market = Market('data/market_data.parquet')

    trading_monkey(monkey, market)
