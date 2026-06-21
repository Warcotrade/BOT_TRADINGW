import config
from find_SL_TP import find_SL_TP

def main():
    print("Bot_tradingW started")

    result = find_SL_TP(entry_price=100.0, direction="long")
    print(result)

    result_short = find_SL_TP(entry_price=100.0, direction="short")
    print(result_short)

if __name__ == "__main__":
    main()
