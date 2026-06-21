def calcular_sl_tp(precio_entrada, sl_porcentaje, tp_porcentaje):
    sl = precio_entrada * (1 - sl_porcentaje / 100)
    tp = precio_entrada * (1 + tp_porcentaje / 100)
    return sl, tp
