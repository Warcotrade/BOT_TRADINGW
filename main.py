import config
from find_SL_TP import calcular_sl_tp

def main():
    print("Bot_tradingW iniciado")

    precio = 100.0
    sl, tp = calcular_sl_tp(precio, config.SL_PORCENTAJE, config.TP_PORCENTAJE)
    print(f"Precio entrada: {precio}")
    print(f"Stop Loss: {sl:.2f} ({config.SL_PORCENTAJE}%)")
    print(f"Take Profit: {tp:.2f} ({config.TP_PORCENTAJE}%)")

if __name__ == "__main__":
    main()
