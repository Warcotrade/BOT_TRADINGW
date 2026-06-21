from config import STOP_LOSS_PERCENT, TARGET_PERCENT

def find_SL_TP(entry_price, direction="long", stop_loss_percent=None, target_percent=None):
    stop_loss_percent = STOP_LOSS_PERCENT if stop_loss_percent is None else stop_loss_percent
    target_percent = TARGET_PERCENT if target_percent is None else target_percent
    direction = direction.lower()

    sl_mult = stop_loss_percent / 100
    tp_mult = target_percent / 100

    if entry_price <= 0:
        raise ValueError("entry_price must be greater than 0")

    if direction == "long":
        stop_loss = entry_price * (1 - sl_mult)
        target = entry_price * (1 + tp_mult)
    elif direction == "short":
        stop_loss = entry_price * (1 + sl_mult)
        target = entry_price * (1 - tp_mult)
    else:
        raise ValueError("direction must be 'long' or 'short'")

    return {
        "entry_price": entry_price,
        "direction": direction,
        "stop_loss": round(stop_loss, 6),
        "target": round(target, 6),
    }
