import pandas_ta as ta
import pandas as pd

def golden_death_cross(monkey, market, reinvest=False):

    #first calculate emas
    ema50 = market.market['Close']['KO'].to_frame(name='Close').ta.ema(50)
    ema200 = market.market['Close']['KO'].to_frame(name='Close').ta.ema(200)

    market.market['ema50'] = ema50
    market.market['ema200'] = ema200

    #drop nan's to have a clear ema chart
    market.market = market.market.dropna(axis=0, how='any')

    market.move()
    market.move()
    market.move()
    market.move()
    market.move()
    market.move()
    market.move()
    market.move()


    while not market.end:
        date, prices = market.now()

        ticker = prices.index[0][1]
        price_today = prices.iloc[0]

        amount_buy = monkey.fiat
        amount_sell = 0

        if ticker in monkey.assets:
            amount_sell = monkey.assets[ticker]['amount'] * price_today

        prev_date = date - pd.Timedelta(days=1)

        #calculate prev ema
        while not prev_date in market.market.index:
            prev_date = prev_date - pd.Timedelta(days=1)

        prev_ema50 = market.market.loc[prev_date]['ema50'].item()
        prev_ema200 = market.market.loc[prev_date]['ema200'].item()

        current_ema50 = market.market.loc[date]['ema50'].item()
        current_ema200 = market.market.loc[date]['ema200'].item()

        #golden cross
        if prev_ema50 < prev_ema200 and current_ema50 >= current_ema200:
            monkey.buy(asset=ticker, amount=amount_buy, price=price_today, date=date)
        #death cross
        elif prev_ema50 > prev_ema200 and current_ema50 <= current_ema200:
            monkey.sell(asset=ticker, amount=amount_sell, price=price_today, date=date)

        market.move()
