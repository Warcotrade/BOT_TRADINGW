import config
from find_SL_TP import find_SL_TP

def main():
    print("Bot_tradingW iniciado")

    resultado = find_SL_TP(entry_price=100.0, direction="long")
    print(resultado)

    resultado_short = find_SL_TP(entry_price=100.0, direction="short")
    print(resultado_short)

if __name__ == "__main__":
    main()
