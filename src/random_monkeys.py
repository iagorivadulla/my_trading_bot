from src.account import Account
from src.markets import Market, read_market
import random
from pathlib import Path

#BASE_DIR = Path(__file__).resolve().parent
#DATA_DIR = BASE_DIR / 'data' / 'market_data_KO.parquet'

#market = Market(DATA_DIR)
#tickers = list(market.market['Close'].columns)

def random_choice(market):
    actions = ['buy', 'sell', 'hold']
    tickers = list(market.market['Close'].columns)
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
        action, ticker = random_choice(market)
        money = random_money(monkey) / prices[ticker][0]
        amount = random_amount(monkey, ticker)

        for t in prices:
            if prices[t][1] is not None:
                for asset in monkey.assets:
                    if t == asset:
                        monkey.add_fiat(prices[t][1] * monkey.assets[asset]['amount'])
                        print(f'{t} has paid {prices[t][1] * monkey.assets[asset]['amount']} USD.')


        if action == 'buy':
            monkey.buy(asset=ticker, amount = money  ,price=prices[ticker][0], date=date)

        elif action == 'sell':
            monkey.sell(asset=ticker, amount=amount, price=prices[ticker][0], date=date)

        elif action == 'hold':
            pass

        market.move()


if __name__ == '__main__':
    monkey = Account(5000)
    market = Market('data/market_data.parquet')

    trading_monkey(monkey, market)
