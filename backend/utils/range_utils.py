def parse_range(range_text: str):
    try:
        low, high = range_text.replace("–", "-").split("-")
        return float(low.strip()), float(high.strip())
    except:
        return None, None

def evaluate_value(value: float, low: float, high: float):
    if value < low:
        return "LOW"
    if value > high:
        return "HIGH"
    return "NORMAL"
