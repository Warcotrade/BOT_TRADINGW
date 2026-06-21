import yfinance as yf
import config
from find_SL_TP import find_SL_TP

def get_bitcoin_price():
    ticker = yf.Ticker("BTC-USD")
    data = ticker.history(period="1d")
    return round(data["Close"].iloc[-1], 2)

def main():
    print("Bot_tradingW started")

    btc_price = get_bitcoin_price()
    print(f"Bitcoin price: ${btc_price}")

    result_long = find_SL_TP(entry_price=btc_price, direction="long")
    print("Long:", result_long)

    result_short = find_SL_TP(entry_price=btc_price, direction="short")
    print("Short:", result_short)

if __name__ == "__main__":
    main()
