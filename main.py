import config
from market_data import get_bitcoin_price
from find_SL_TP import find_SL_TP

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
