import yfinance as yf

def get_bitcoin_price():
    ticker = yf.Ticker("BTC-USD")
    data = ticker.history(period="1d")
    return float(round(data["Close"].iloc[-1], 2))
