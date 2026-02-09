def parse_reference_range(text):
    text = text.replace("–", "-").strip()

    try:
        if "-" in text:
            low, high = text.split("-")
            return float(low), float(high)

        if text.startswith("<"):
            return None, float(text.replace("<", ""))

        if text.startswith(">"):
            return float(text.replace(">", ""))

    except:
        pass

    return None, None
