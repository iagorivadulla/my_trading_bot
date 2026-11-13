import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

def market_data(ticker, start: str, end: str, interval: str ,auto_adjust=False):

        data = yf.download(
                    ticker,
                    start = start,
                    end = end,
                    auto_adjust = auto_adjust,  # this would add dividens to price
                    interval = interval,
                    actions=True)

        return data